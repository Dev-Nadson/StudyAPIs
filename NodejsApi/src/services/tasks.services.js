import db from '../repositories/index.js'

async function createTask(data) {
    return db.create(data)
}

async function listTasks(search) {
    return db.list(search)
}

async function updateTask(id, data) {
    return db.update(id, data)
}

async function deleteTask(id) {
    return db.delete(id)
}

export default { createTask, listTasks, updateTask, deleteTask }
