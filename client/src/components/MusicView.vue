<template>
	<div>
		<div
			class="card playlist-card"
			:key="playlist.id"
			v-for="playlist in playlists"
		>
			<div class="container-grid image-wrapper">
				<img :src="playlist.album_image" />
			</div>
			<div class="info flex-col">
				<h3>{{ playlist.album_name }}</h3>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: 'MusicView',
	components: {
		// musicCard,
	},
	props: {
		playlists: {},
	},
};
</script>

<style scoped>
.item-view-content {
	display: flex;
	flex-direction: column;
	width: 100%;
}

.user-info img {
	border-radius: 50%;
}

.user-info h3 {
	margin-left: 1em;
}

.item-view-content img {
	max-height: 800px;
	margin: auto;
}

.photo-container {
	margin: auto;
	padding: 1em;
}

.stats {
	justify-content: space-between;
	width: 80%;
	margin: auto;
	border-bottom: 1px solid rgba(0, 0, 0, 0.3);
}

.row {
	display: flex;
	align-items: center;
	flex-wrap: wrap;
}

.badge {
	width: 80%;
	margin: auto;
	align-items: flex-start !important;
	justify-content: flex-start;
}

.badge span {
	background-color: rgba(0, 191, 166, 0.3);
	margin: 0.5em;
	padding: 0.4em 0.6em;
	border-radius: 8px;
}

.icon {
	font-size: 1.4rem;
}
</style>
