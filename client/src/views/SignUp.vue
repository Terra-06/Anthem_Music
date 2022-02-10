<template>
	<div class="sign-up">
		<h1>Sign Up</h1>

		<form @submit.prevent="submitForm">
			<input
				type="text"
				name="firstName"
				placeholder="First Name"
				v-model="firstName"
			/>

			<input
				type="text"
				name="lastName"
				placeholder="Last Name"
				v-model="lastName"
			/>

			<input
				type="text"
				name="username"
				placeholder="Username"
				v-model="username"
			/>
			<input
				type="password"
				name="password"
				placeholder="Password"
				v-model="password"
			/>

			<input
				type="email"
				name="email"
				placeholder="example@example.com"
				v-model="email"
			/>
			<button type="submit">Sign Up</button>
		</form>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'SignUp',
	data() {
		return {
			firstName: '',
			lastName: '',
			username: '',
			password: '',
			email: '',
		};
	},
	methods: {
		submitForm() {
			const formData = {
				firstName: this.firstName,
				lastName: this.lastName,
				username: this.username,
				password: this.password,
				email: this.email,
			};

			axios
				.post('/api/v1/users/', formData)
				.then((response) => {
					this.$router.push('/log-in');
					console.log(response);
				})
				.catch((error) => {
					console.log(error);
				});
		},
	},
};
</script>

<style>
.sign-up {
	color: #7dd526;
}
</style>
