# project_management.py
import datetime

from project import Project


def load_projects(filename):
    projects = []
    try:
        with open(filename, 'r') as file:
            next(file)  # skip header
            for line in file:
                data = line.strip().split('\t')
                project = Project(*data)
                projects.append(project)
        print("Projects loaded successfully.")
    except FileNotFoundError:
        print("File not found. No projects loaded.")
    return projects


def save_projects(filename, projects):
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t"
                       f"{project.cost_estimate}\t{project.completion_percentage}\n")
    print("Projects saved successfully.")


def display_projects(projects):
    incomplete = [project for project in projects if project.completion_percentage < 100]
    completed = [project for project in projects if project.completion_percentage == 100]

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def filter_projects_by_date(projects, filter_date):
    try:
        filter_date = datetime.datetime.strptime(filter_date, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > filter_date]
        print("Filtered projects:")
        for project in filtered_projects:
            print(f"  {project}")
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")


def add_new_project(projects):
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    completion_percentage = input("Percent complete: ")

    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(project)
    print(f"Project '{name}' added successfully.")


def update_project(projects):
    display_projects(projects)
    try:
        choice = int(input("Project choice: "))
        if 0 <= choice < len(projects):
            project = projects[choice]
            print(project)
            new_percentage = input("New Percentage: ")
            new_priority = input("New Priority: ")
            if new_percentage:
                project.completion_percentage = int(new_percentage)
            if new_priority:
                project.priority = int(new_priority)
            print("Project updated successfully.")
        else:
            print("Invalid project choice.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def main():
    projects = load_projects("projects.txt")

    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        choice = input(">>> ").upper()

        if choice == "L":
            load_projects_filename = input("Enter filename to load projects from: ")
            projects = load_projects(load_projects_filename)
        elif choice == "S":
            save_projects_filename = input("Enter filename to save projects to: ")
            save_projects(save_projects_filename, projects)
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_date = input("Enter filter date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, filter_date)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        elif choice == "Q":
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
