module.exports = {
  rootDir: '.',
  testEnvironment: 'jsdom',
  transform: {
    '^.+\\.[jt]sx?$': 'babel-jest',
  },
  setupFilesAfterEnv: ['@testing-library/jest-dom'],
  moduleNameMapper: {
    '\\.css$': 'identity-obj-proxy',
    '@docusaurus/(.*)': '<rootDir>/node_modules/@docusaurus/core/lib/client/exports/$1',
  },
  transformIgnorePatterns: [
    '/node_modules/(?!@docusaurus/.*)',
  ],
  testPathIgnorePatterns: ['/node_modules/', '/.docusaurus/'],
};
