module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:8000', // L'URL de votre serveur backend Django
        ws: true,
        changeOrigin: true
      },
    }
  }
};