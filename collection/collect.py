from main.models import Company, JobPosting, Skill

# Use model manager big_companies for the model Company
def get_big_companies():  
    return(", ".join(c[1]['name'] for c in enumerate(Company.big_companies.all().values())))

def working_with_models():
    # values["n"]
    # 1. Access the name of a choice field option
    # 2. hasattr to check an object has an attribute
    
    values = {}

    values["1"] = (
        'Access the name of a choice field option',
        JobPosting.objects.first().level,
        JobPosting.objects.first().get_level_display()
    )  

    jp = JobPosting.objects.first()
    values["2"] = (    
        'hasattr can be used with an object to check if it has a specified attribute',
        {'hasattr(jp, \'something\')': hasattr(jp, 'something'),
        'hasattr(jp, \'level\')': hasattr(jp, 'level')
        }
    )
    return values