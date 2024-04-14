const CopyPlugin = require('copy-webpack-plugin');

module.exports = {
  webpack: (config, { isServer }) => {
    if (!isServer) {
      config.plugins.push(
        new CopyPlugin({
          patterns: [
            { from: './python/app.py', to: './web/src/app/page.js' },
          ],
        }),
      );
    }
    return config;
  },
};