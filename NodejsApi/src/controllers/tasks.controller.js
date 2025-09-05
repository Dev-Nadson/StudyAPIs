import taskService from '../services/tasks.services.js'

async function create(req, reply) {
    const { title, description } = req.body
    await taskService.createTask({
        title: title,
        description: description
    })
    return reply.status(201).send()
}

async function list(req, reply) {
    const search = req.query.search
    const tasks = await taskService.listTasks(search)
    return reply.send(tasks)
}

async function update(req, reply) {
    const taskID = req.params.id
    const { title, description } = req.body
    await taskService.updateTask(taskID, { title, description })
    return reply.send()
}

async function remove(req, reply) {
    const taskID = req.params.id
    await taskService.deleteTask(taskID)
    return reply.status(204).send()
}

export default { create, list, update, remove }
