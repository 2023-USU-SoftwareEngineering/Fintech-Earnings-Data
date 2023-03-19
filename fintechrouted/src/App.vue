<template>
  <div class="homepage">
    <div class="content">
      <div class="menu">
        <div class="menu-item">
          <div class="menu-text">
            <router-link to="/pricetrend" class="link">Price Trend</router-link>
          </div>
        </div>
        <div class="menu-item">
          <div class="menu-text">
            <router-link to="/pricehistory" class="link">Price History</router-link>
          </div>
        </div>
        <div class="menu-item menu-center">
          <router-link to="/" class="homelink">Home</router-link>
        </div>
        <div class="menu-item">
          <div class="menu-text">
            <router-link to="/aboutus" class="link">About us</router-link>
          </div>
        </div>
        <div class="menu-item">
          <div class="menu-text">
            <router-link to="/contact" class="link">Contact</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  color: white;
  /* margin-top:60px; */
}
body {
  background: #080808;
  background-image: url("./assets/city.gif");
  background-size: cover;
  height: 100vh;
  padding:0;
  margin:0;
}

.menu {
  display: flex;
  align-items: center;
  justify-content: space-around;
  margin-top: 10px;
}

.menu-item {
  flex: 1;
  text-align: center;
}

.menu-text {
  font-size: 20px;
  color: #818181;
  cursor: pointer;
  padding: 10px;
  border-bottom: 2px solid #080808;
  width: fit-content;
  margin: auto;
}

.menu-text:hover {
  border-bottom: 2px solid #c278ff;
}

/*.menu-center {
  font-size: 30px;
  color: #EAEAEA;
}*/

.menu-center:hover {
  border-bottom: 2px solid #c278ff;
  cursor: pointer;
}

.link {
  color: #818181;
  text-decoration: none;
}

.homelink {
  font-size: 30px;
  color: #EAEAEA;
  text-decoration: none;
}
</style>
