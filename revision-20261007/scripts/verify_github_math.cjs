#!/usr/bin/env node
'use strict';
// Verify every emitted GitHub formula with base + ams + newcommand only.
// No network access or global package installation is used.
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const root = path.resolve(__dirname, '..');
const argument = process.argv.indexOf('--mathjax');
const mj = argument >= 0 ? path.resolve(process.argv[argument + 1]) :
  process.env.MATHJAX_PATH || path.join(root, 'node_modules', 'mathjax-full');
if (!mj) throw new Error('Provide --mathjax PACKAGE_PATH or MATHJAX_PATH');
const req = (file) => require(path.join(mj, 'js', file));
const version = require(path.join(mj, 'package.json')).version;
const {mathjax} = req('mathjax.js');
const {TeX} = req('input/tex.js');
const {SVG} = req('output/svg.js');
const {liteAdaptor} = req('adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = req('handlers/html.js');
for (const file of ['base/BaseConfiguration.js', 'ams/AmsConfiguration.js',
  'newcommand/NewcommandConfiguration.js']) req('input/tex/' + file);
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
let errors = [];
const tex = new TeX({
  packages: ['base', 'ams', 'newcommand'], tags: 'ams', maxBuffer: 100000,
  formatError: (_jax, error) => {
    errors.push(String(error.message || error));
    throw error;
  },
});
const document = mathjax.document('', {
  InputJax: tex, OutputJax: new SVG({fontCache: 'none'}),
});
const inputPath = path.join(root, 'qa', 'GitHub-build.json');
const bytes = fs.readFileSync(inputPath);
const input = JSON.parse(bytes.toString('utf8'));
const hash = (data) => crypto.createHash('sha256').update(data).digest('hex');
const result = {
  status: 'PASS', renderer: 'MathJax ' + version,
  packages: ['base', 'ams', 'newcommand'],
  input: 'qa/GitHub-build.json', input_sha256: hash(bytes),
  check: 'Every emitted formula converted to SVG; TeX errors and merror nodes inspected',
  documents: [], total_formula_count: 0,
};
for (const item of input.documents) {
  const failures = [];
  let rendered = 0;
  for (const formula of item.formulas) {
    errors = [];
    result.total_formula_count++;
    try {
      const node = document.convert(formula.github_tex, {
        display: formula.kind === 'display',
      });
      const html = adaptor.outerHTML(node);
      if (errors.length || /data-mjx-error|<merror|mjx-merror/.test(html)) {
        failures.push({index: formula.index, source_line: formula.source_line,
          errors: errors.slice()});
      } else rendered++;
    } catch (error) {
      failures.push({index: formula.index, source_line: formula.source_line,
        errors: [String(error)]});
    }
  }
  result.documents.push({
    source: item.source, source_sha256: item.source_sha256,
    target: item.target, target_sha256: item.target_sha256,
    formula_count: item.formula_count,
    equation_tag_count: item.equation_tag_count,
    rendered_svg_count: rendered, errors: failures,
  });
  if (failures.length) result.status = 'FAIL';
}
fs.writeFileSync(path.join(root, 'qa', 'GitHub-mathjax-base.json'),
  JSON.stringify(result, null, 2) + '\n', 'utf8');
console.log(JSON.stringify(result));
if (result.status !== 'PASS') process.exitCode = 1;
