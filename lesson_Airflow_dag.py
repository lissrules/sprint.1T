from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

def hello():
    print("Airflow")
def generation():
    import random
    i1=random.randrange(1, 100)
    i2=random.randrange(1, 100)
    str1 = str(i1) + " " + str(i2)
    print(str1)
    f=open(file='my.txt', mode = 'a')
    f.write(str1 +'\n')
    f.close()

def readandcalc():
    f=open(file='my.txt', mode = 'r')
    x1=0
    x2=0
    for line in f:
        x = line.split(" ")
        if len(x)==2:
            x1=x1+int(x[0])
            x2=x2+int(x[1])
    f.close()
    f=open(file='my.txt', mode = 'a')
    f.write(str(x1-x2)+'\n')
    print(str(x1-x2)+'\n')
    f.close()

def truncfile():
    f=open(file='my.txt', mode = 'r')
    lines = f.readlines()
    f.close()
    print (str(len(lines)))
    with open('my.txt', 'w') as f:
        for line in lines[:-1]:
            f.write(f"{line}")




with DAG(dag_id="_first_dag", start_date=datetime(2022,12,4), schedule_interval="* * * * *", max_active_runs=5) as dag:
    bash_task=BashOperator(task_id = "task_hello", bash_command="echo HELLO!")
    python_task=PythonOperator(task_id = "task_world", python_callable=hello)
    python_task_gen=PythonOperator(task_id = "task_generate", python_callable=generation)
    python_task_calc=PythonOperator(task_id = "task_calculate", python_callable=readandcalc)
    python_task_trunc=PythonOperator(task_id = "task_truncfile", python_callable=truncfile)


bash_task>>python_task>>python_task_gen>>python_task_calc>>python_task_trunc
