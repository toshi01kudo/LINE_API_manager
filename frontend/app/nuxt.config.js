export default {
    server: {
      port: 19250,
      host: "0.0.0.0",
    },
    buildModules: [
      "@nuxtjs/vuetify",
    ],
    ssr: true,
    target: "server",
    head: {
      titleTemplate: "LINE-API-Manager"
    }
  }