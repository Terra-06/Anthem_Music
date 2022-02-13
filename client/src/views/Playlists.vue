////
/2.0/?method=user.getweeklychartlist&user=rj&api_key=YOUR_API_KEY&format=json
////2.0/?method=user.getweeklytrackchart&user=rj&api_key=YOUR_API_KEY&format=json

<template>
	<div class="playlists">
		<h1>Playlists</h1>
	</div>
</template>

<script>
import axios from 'axios';
import { MUSIC_URL } from '../globals';
console.log(MUSIC_URL);
const API_KEY = process.env.VUE_APP_MUSIC_API_KEY;
console.log(API_KEY);
// import MusicCard from '../components/MusicCard.vue';
// import MusicView from '../components/MusicView.vue';

export default {
	name: 'Playlist',
	components: {
		// MusicCard,
		// MusicView,
	},
	data: () => ({
		chartList: {},
		trackChart: [],
	}),

	mounted: function () {
		this.getChartList();
		console.log('working');
	},

	methods: {
		async getChartList() {
			const response = await axios.get(
				`${MUSIC_URL}2.0/?method=user.getweeklychartlist&user=rj&api_key${API_KEY}&format=json`
			);
			this.chartList = response.data;
			console.log(response);
		},
		async getTrackChart() {
			const result = await axios.get(
				`${MUSIC_URL}2.0/?method=user.getweeklytrackchart&user=rj&api_key=${API_KEY}&format=json`
			);
			this.trackChart = result.data;
		},
	},
};
</script>

<style>
.playlists {
	color: #7dd526;
}
</style>
