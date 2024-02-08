# Force LF everywhere for prettier
* text eol=lf
# Ignore diffs in dist as it is generated code
dist/** -diff linguist-generated=truedist/
lib/
node_modules/
tsconfig.json{
  "root": true,
  "plugins": [
    "jest",
    "@typescript-eslint",
    "prettier",
    "github ],
  "extends": [
    "plugin:github/recommended",
    "plugin:github/typescript",
    "prettier" ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": 9,
    "sourceType": "module",
    "project": "./tsconfig.eslint.json" },
  "rules": {
    "prettier/prettier": "error",
    "filenames/match-regex": [
      "error"
             ["][a-]0][-9-]
  
                    +(.test
                      [)?$],
    "i18n-text/no-en": "off",
    "eslint-comments/no-use": "off",
    "import/no-namespace": "off",
    "no-unused-vars": "off",
    "@typescript-eslint/no-unused-vars": [
      "error" ],
    "@typescript-eslint/explicit-member-accessibility": [
      "error", {
        "accessibility": "public" }],
    "no-shadow": "off",
    "@typescript-eslint/no-shadow": [
      "error"],
    "@typescript-eslint/no-require-imports": "error",
    "@typescript-eslint/array-type": "error",
    "@typescript-eslint/await-thenable": "error",
    "@typescript-eslint/ban-ts-comment": "error",
    "camelcase": "off",
    "@typescript-eslint/consistent-type-assertions": "error",
    "@typescript-eslint/explicit-function-return-type": [
      "error", {
        "allowExpressions": true}  ],  "@typescript-eslint/func-call-spacing": [
      "error",
      "never" ],
    "@typescript-eslint/no-array-constructor": "error",
    "@typescript-eslint/no-empty-interface": "error",
    "@typescript-eslint/no-explicit-any": "error",
    "@typescript-eslint/no-extraneous-class": "error",
    "@typescript-eslint/no-for-in-array": "error",
    "@typescript-eslint/no-inferrable-types": "error",
    "@typescript-eslint/no-misused-new": "error",
    "@typescript-eslint/no-namespace": "error",
    "@typescript-eslint/no-non-null-assertion": "warn",
    "@typescript-eslint/no-unnecessary-qualifier": "error",
    "@typescript-eslint/no-unnecessary-type-assertion": "error",
    "@typescript-eslint/no-useless-constructor": "error",
    "@typescript-eslint/no-var-requires": "error",
    "@typescript-eslint/prefer-for-of": "warn",
    "@typescript-eslint/prefer-function-type": "warn",
    "@typescript-eslint/prefer-includes": "error",
    "@typescript-eslint/prefer-string-starts-ends-with": "error",
    "@typescript-eslint/promise-function-async": "error",
    "@typescript-eslint/require-array-sort-compare": "error",
    "@typescript-eslint/restrict-plus-operands": "error",
    "semi": "off",
    "@typescript-eslint/semi": [
      "error",
      "never"],
    "@typescript-eslint/type-annotation-spacing": "error",
    "@typescript-eslint/unbound-method": "error"  },
  "env": {
    "node": true,
    "es6": true,
    "jest/globals": true  }
}dist/
lib/
node_modules/
tsconfig.jsondist/
lib/
node_modules/
jest.config.js
{
  "printWidth": 80,
  "tabWidth": 2,
  "useTabs": false,
  "semi": false,
  "singleQuote": true,
  "trailingComma": "none",
  "bracketSpacing": false,
  "arrowParens": "avoid"
}
