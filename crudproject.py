Students = []

while True:

    print("\n -------- Select your choice -------")
    print("1. Add student")
    print("2. Display Students")
    print("3. Update student")
    print("4. Delete student")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        student_id = int(input("Enter student's roll number: "))
        name = input("Enter student's name: ")
        age = int(input("Enter student's age: "))
        city = input("Enter student's city: ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "city": city
        }

        Students.append(student)

        print("Student added successfully!!!!")

    elif choice == 2:

        print("\nStudents List")

        for student in Students:
            if len(Students) == 0:
                print("List is empty")
            else:

                print(f"ID : {student['id']}")
                print(f"Student Name : {student['name']}")
                print(f"Age : {student['age']}")
                print(f"City : {student['city']}")
                print()

    elif choice == 3:
        id = int(input("Enter the student's roll number to update: "))

        for student in Students:

            if id == student['id']:
                student['name'] = input("Enter updated name : ")
                student['age'] = int(input("Enter updated age : "))
                student['city'] = input("Enter updated city: ")

        print("\n Student updated sucessfully !!!")

    elif choice == 4:

        id = int(input("Enter the student's roll number to delete : ")) 

        for student in Students:

            if id == student['id']:
                Students.remove(student)

        print("Deleted Sucessfully!!!!")

    elif choice == 5:
        print("Program exited!!")
        break

        
    else:
        print("Invalid choice!")


# For product management
products = []

while True:

    print("\n------ PRODUCT MANAGEMENT SYSTEM ------")
    print("1. Add Product")
    print("2. Display Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # CREATE
    if choice == 1:

        product_id = int(input("Enter product ID: "))
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter quantity: "))

        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)

        print("Product added successfully!")

    # READ
    elif choice == 2:

        if len(products) == 0:
            print("No products available.")

        else:
            print("\n------ PRODUCT LIST ------")

            for product in products:
                print("ID       :", product["id"])
                print("Name     :", product["name"])
                print("Price    :", product["price"])
                print("Quantity :", product["quantity"])
                print("-------------------------")

    # UPDATE
    elif choice == 3:

        product_id = int(input("Enter product ID to update: "))

        for product in products:

            if product["id"] == product_id:

                product["name"] = input("Enter new product name: ")
                product["price"] = float(input("Enter new price: "))
                product["quantity"] = int(input("Enter new quantity: "))

                print("Product updated successfully!")
                
    # DELETE
    elif choice == 4:

        product_id = int(input("Enter product ID to delete: "))

        for product in products:

            if product["id"] == product_id:

                products.remove(product)

                print("Product deleted successfully!")

    # EXIT
    elif choice == 5:

        print("Thank you!")
        break

    else:
        print("Invalid choice!")