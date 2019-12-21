'use strict';
// Template version: 1.3.1
// see http://vuejs-templates.github.io/webpack for documentation.

const path = require('path');

module.exports = {
  dev: {
    // Paths
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',
    proxyTable: {
      '/auth/': {
          target: 'http://api:5000', // if it is localhost:5000, which means the client(front-end side) will roast itself inside its own container. Because there is nothing here.
          changeOrigin: true,
      },
      '/auth/register': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/auth/get-user': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/auth/update-password': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/handling/upload': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/student-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/create-student-record': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/remove-student-record': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/update-student-record': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/student-status-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/remove-student-status-record': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/search-student-record': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/student/create-student-subject': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/subject/subject-records': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/subject/create-subject': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/subject/edit-subject': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/subject/remove-subject': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/subject/search-subject': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/log/log-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/create-semester': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/remove-semester': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/edit-semester': {
        target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/semester-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/register-semester-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/create-shift': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/remove-shift': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/edit-shift': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/shift-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/room-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/update-room':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/remove-room':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/create-room':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/schedule/student-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/room/room-records': {
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/room/update-room-record':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/room/remove-room-record':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/room/create-room-records':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/room/search-room-record':{
          target: 'http://api:5000',
          changeOrigin: true,
      },
      '/shift-register/shift-records':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/search-semester':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/search-subject':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/room-records':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/registered-room-records':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/register-shift': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/registered-room-shift-records':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/get-info': {
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/export-records':{
        target: 'http://api:5000',
        changeOrigin: true,
      },
      '/shift-register/remove-export-records':{
        target: 'http://api:5000',
        changeOrigin: true,
      }
    },

    // Various Dev Server settings
    host: '0.0.0.0', // can be overwritten by process.env.HOST
    port: 8080, // can be overwritten by process.env.PORT, if port is in use, a free one will be determined
    autoOpenBrowser: false,
    errorOverlay: true,
    notifyOnErrors: true,
    poll: false, // https://webpack.js.org/configuration/dev-server/#devserver-watchoptions-


    /**
     * Source Maps
     */

    // https://webpack.js.org/configuration/devtool/#development
    devtool: 'cheap-module-eval-source-map',

    // If you have problems debugging vue-files in devtools,
    // set this to false - it *may* help
    // https://vue-loader.vuejs.org/en/options.html#cachebusting
    cacheBusting: true,

    cssSourceMap: true
  },

  build: {
    // Template for index.html
    index: path.resolve(__dirname, '../dist/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../dist'),
    assetsSubDirectory: 'static',
    assetsPublicPath: '/',

    /**
     * Source Maps
     */

    productionSourceMap: true,
    // https://webpack.js.org/configuration/devtool/#production
    devtool: '#source-map',

    // Gzip off by default as many popular static hosts such as
    // Surge or Netlify already gzip all static assets for you.
    // Before setting to `true`, make sure to:
    // npm install --save-dev compression-webpack-plugin
    productionGzip: false,
    productionGzipExtensions: ['js', 'css'],

    // Run the build command with an extra argument to
    // View the bundle analyzer report after build finishes:
    // `npm run build --report`
    // Set to `true` or `false` to always turn it on or off
    bundleAnalyzerReport: process.env.npm_config_report
  }
};
