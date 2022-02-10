<template>
	<div class="app">
		<div id="nav">
			<router-link to="/sign-up"> Sign Up | </router-link>
			<router-link to="/log-in"> Log In </router-link>
		</div>
		<router-view />
	</div>
</template>

<script>
export default {
	name: 'App',
	components: {},
};
</script>

<style>
#app {
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	text-align: center;
	color: #2c3e50;
	margin-top: 60px;
}

#nav {
	padding: 60px;
}
</style>
