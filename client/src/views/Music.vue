<template>
	<div class="music">
		<h1>Music Page</h1>
	</div>
</template>

<script>
import axios from 'axios';
import { MUSIC_URL } from '../globals';
console.log(MUSIC_URL);
const API_KEY = process.env.VUE_APP_MUSIC_API_KEY;
console.log(API_KEY);
// import MusicCard from '../components/MusicCard.vue';
// import MusicView from './MusicView.vue';

export default {
	name: 'Music',
	components: {
		// MusicCard,
		// MusicView,
	},
	data: () => ({
		// currentMusic: {},
		chartMusic: [],
	}),

	mounted: function () {
		this.getChartMusic();
		console.log('working');
	},

	methods: {
		async getChartMusic() {
			const response = await axios.get(
				`${MUSIC_URL}2.0/?method=chart.gettoptracks&api_key=${API_KEY}&format=json`
			);
			this.chartMusic = response.data;
			console.log(response);
		},
		// async getCurrentMusic(musicId) {
		// 	const result = await axios.get(
		// 		`${MUSIC_URL}/photos/${musicId}?client_id=${API_KEY}`
		// 	);
		// 	this.currentMusic = result.data;
		// },
	},
};
</script>

<style>
.music {
	color: #7dd526;
}
</style>
