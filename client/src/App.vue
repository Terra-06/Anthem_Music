<template>
	<div class="app">
		<div id="nav">
			<router-link to="/sign-up"> Sign Up || </router-link>
			<router-link to="/log-in"> Log In || </router-link>
			<router-link to="/music"> Music || </router-link>
			<router-link to="/playlists"> Playlists </router-link>
		</div>
		<router-view />
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'App',
	beforeCreate() {
		this.$store.commit('initializeStore');

		const token = this.$store.state.token;

		if (token) {
			axios.defaults.headers.common['Authorization'] = 'Token ' + token;
		} else {
			axios.defaults.headers.common['Authorization'] = '';
		}
	},
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
