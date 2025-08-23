import sql from './db.js'

sql`
CREATE TABLE tasks (
    id VARCHAR(255) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT
);`
    .then(() => {
        console.log("table created")
    })