import taskController from '../controllers/tasks.controller.js'

async function taskRoutes(fastify) {
    fastify.post('/tasks', taskController.create)
    fastify.get('/tasks', taskController.list)
    fastify.put('/tasks/:id', taskController.update)
    fastify.delete('/tasks/:id', taskController.remove)
}

export default taskRoutes