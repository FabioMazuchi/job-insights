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


# filter_by_job_type("j", "OTHER")

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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
