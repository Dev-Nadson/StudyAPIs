import Fastify from 'fastify'
import taskRoutes from './src/routes/tasks.routes.js'

export async function buildApp() {
    const app = Fastify()
    app.register(taskRoutes)
    return app
}