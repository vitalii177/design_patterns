import datetime
import lab_1 as l

def main():
    developer = l.Developer(id=1, name="Vitalii Maksymchuk",
                          address="Dnisterska Street, 2",
                          phone_number="+38 (063) 296-11-39",
                          email="vitaliimaksymchuk53@gmail.com",
                          position="Junior", rank="",
                          salary=1100.0)

    project = l.Project(title="Learning Project", start_date=datetime.datetime.now())
    developer.assign(project_to_assign=project)

if __name__ == "__main__":
    main()