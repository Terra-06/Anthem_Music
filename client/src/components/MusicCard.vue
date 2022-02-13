<template>
	<div>
		<div class="card music-card" @click="selectMusic(music.id)">
			<div class="image-wrapper">
				<img :src="music.album_image" />
			</div>
			<div class="info flex-col">
				<h3>{{ music.genre }}</h3>
			</div>
		</div>
	</div>
</template>

// :key="music.id" // v-for="music in chartMusic"
<script>
export default {
	name: 'MusicCard',
	props: {
		// ['music'],
		chartMusic: [],
		// playlists: {},
	},
	methods: {
		selectTrack(musicId) {
			this.$emit('getChartMusic', musicId);
		},
	},
};
</script>

<style scoped>
.card {
	border: 1px solid;
	border-radius: 8px;
	max-width: 400px;
	margin: 1em auto;
	cursor: pointer;
	transition: all 0.2s ease;
}

.card:hover {
	opacity: 0.7;
}
.icon {
	font-size: 1.3rem;
}

.card-header {
	display: flex;
	align-items: center;
	justify-content: space-between;
	padding: 1em 0.5em;
}

.info {
	display: flex;
	align-items: center;
}

.card-header h3 {
	margin-left: 0.5em;
}

.card-header img {
	border-radius: 50%;
}

.card-content {
	text-align: center;
}
</style>
