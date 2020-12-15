<template>
  <div id="app">
    <div id="nav">
      <router-link to="/calculate"> Посчитать </router-link> |
      <router-link to="/calculate-max-sale"> Максимальная точка цены реализации </router-link> |
      <router-link to="/calculate-zero-profitability"> Точка нулевой рентабельности </router-link> |
      <router-link to="/table"> Таблица </router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
