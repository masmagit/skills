from main.models import Skill, Category, JobPosting

def delete_rec(method, **value):
    try:
        rec = method(**value)
        rec.delete()
    except:
        pass

def clean_data():
    # clean add_data()
    delete_rec(Category.objects.get, name="Category1")
    delete_rec(Skill.objects.get, name="Skill1")
    delete_rec(Skill.objects.get, name="Skill2")

def add_data():   
    clean_data()
    
    cat = Category(name="Category1")
    cat.save()
    skill1 = Skill.objects.create(name="Skill1")
    skill2 = Skill.objects.create(name="Skill2")

    # assign foreignkey linked data
    skill1.category = cat
    skill1.save()

    # assign manytomany linked data
    jp = JobPosting.objects.first()
    jp.skills.add(skill1, skill2)

    return (
        skill1.category, jp.skills.all()
    )
