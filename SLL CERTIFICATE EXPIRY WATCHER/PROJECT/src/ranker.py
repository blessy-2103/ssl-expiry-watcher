def rank_domains(results):
    return sorted(results, key=lambda x: x["days_left"])