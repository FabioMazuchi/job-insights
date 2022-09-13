from src.jobs import read


def get_unique_job_types(path):
    lista = read(path)
    result = {}
    for item in lista:
        job = item["job_type"]
        if job not in result:
            result[job] = {"jobs": 0}
        result[job]["jobs"] += 1
    return result


def filter_by_job_type(jobs, job_type):
    result = []
    for row in jobs:
        if row["job_type"] == job_type:
            result.append(row)
    return result


def get_unique_industries(path):
    lista = read(path)
    result = {}
    for item in lista:
        industry = item["industry"]
        if industry != "":
            if industry not in result and industry:
                result[industry] = {"jobs": 0}
            result[industry]["jobs"] += 1
    return result


def filter_by_industry(jobs, industry):
    result = []
    for row in jobs:
        if row["industry"] == industry:
            result.append(row)
    return result


def get_max_salary(path):
    lista = read(path)
    result = []
    for item in lista:
        max_salary = item["max_salary"]
        if max_salary.isdigit():
            result.append(int(max_salary))
    return max(result)


def get_min_salary(path):
    lista = read(path)
    result = []
    for item in lista:
        min_salary = item["min_salary"]
        if min_salary.isdigit():
            result.append(int(min_salary))
    return min(result)


def validate(job, salary):
    if not isinstance(salary, int):
        raise ValueError("isn't a valid integer")

    if "min_salary" not in job.keys() or "max_salary" not in job.keys():
        raise ValueError("min_salary or max_salary doesn't exists")

    min = job["min_salary"]
    max = job["max_salary"]

    if not isinstance(min, int) or not isinstance(max, int):
        raise ValueError("isn't a valid integer")

    if min > max:
        raise ValueError(f"{min} is greather than {max}")


def matches_salary_range(job, salary):
    validate(job, salary)

    min = job["min_salary"]
    max = job["max_salary"]

    if min <= salary <= max:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            matches_salary_range(job, salary)
        except ValueError:
            print("Ocorreu um erro.")
        else:
            if matches_salary_range(job, salary):
                result.append(job)
    return result


jobs = [
    {"max_salary": 0, "min_salary": 10},
    {"max_salary": 10, "min_salary": 100},
    {"max_salary": 10000, "min_salary": 200},
    {"max_salary": 15000, "min_salary": 0},
    {"max_salary": 1500, "min_salary": 0},
    {"max_salary": -1, "min_salary": 10},
]
print(filter_by_salary_range(jobs, 0))
