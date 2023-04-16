from src.jobs import read


def get_unique_job_types(path):
    result = read(path)
    return list(set([row["job_type"] for row in result]))


def filter_by_job_type(jobs, job_type):
    return [job for job in jobs if job["job_type"] == job_type]


def get_unique_industries(path):
    result = read(path)
    return list(
        set([row["industry"] for row in result if row["industry"] != ""])
    )


def filter_by_industry(jobs, industry):
    return [job for job in jobs if job["industry"] == industry]


def get_max_salary(path):
    result = read(path)
    return max(
        [
            int(item["max_salary"])
            for item in result
            if item["max_salary"].isdigit()
        ]
    )


def get_min_salary(path):
    result = read(path)
    return min(
        [
            int(item["min_salary"])
            for item in result
            if item["min_salary"].isdigit()
        ]
    )


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
