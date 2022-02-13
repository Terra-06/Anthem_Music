import { createRouter, createWebHistory } from 'vue-router'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Music from '../views/Music.vue'
import Playlists from '../views/Playlists.vue'

const routes = [
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },


    {
        path: '/log-in',
        name: 'LogIn',
        component: LogIn
    },

    {
        path: '/music',
        name: 'Music',
        component: Music
    },

    {
        path: '/playlists',
        name: 'Playlists',
        component: Playlists
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

export default router