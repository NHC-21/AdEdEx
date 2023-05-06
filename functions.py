import sqlite3
conn = sqlite3.connect('tasks.sqlite')
cursor = conn.cursor()


def addTask(task, member, deadline):
    global cursor

    cursor.execute(f"INSERT INTO tasks (task, member) VALUES ('{task}', '{member}');")
    conn.commit()
def editTask(oldTask, newTask):
    global cursor

    cursor.execute(f"UPDATE tasks SET task = '{newTask}' WHERE task = '{oldTask}';")
    conn.commit()
def editDeadLine(oldMember, newMember):
    global cursor

    cursor.execute(f"UPDATE tasks SET member = '{newMember}' WHERE member = '{oldMember}';")

def editDeadLine(oldDeadLine, newDeadLine):
    global cursor

    cursor.execute(f"UPDATE tasks SET deadline = '{newDeadLine}' WHERE deadline = '{oldDeadLine}';")
def delTask(task):
    global cursor

    cursor.execute(f"DELETE FROM tasks WHERE task = '{task}';")
    conn.commit()

