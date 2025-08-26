"""
Starting template for creating an email simulator program using
classes, methods, and functions.

This template provides a foundational structure to develop your own
email simulator. It includes placeholder functions and conditional statements
with 'pass' statements to prevent crashes due to missing logic.
Replace these 'pass' statements with your implementation once you've added
the required functionality to each conditional statement and function.

Note: Throughout the code, update comments to reflect the changes and logic
you implement for each function and method.
"""

# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.

class Email:
   
    
    # constructor method - class attributes
    def __init__(self, email_address, subject_line, email_content,has_been_read):
        self.email_address = email_address
        self.subject_line  = subject_line
        self.email_content = email_content
        self.has_been_read = has_been_read
        
    def mark_as_read(self):
        has_been_read = True
       
    
      
# Initialise the instance variables for each email.
email_1 = Email('juleiga.regal@gmail.com', 'difficult task', 'python', False)

#print(email_1.email_address)

# Create the 'mark_as_read()' method to change the 'has_been_read'



# instance variable for a specific object from False to True.
email_1.has_been_read = True

# --- Functions --- #
# Build out the required functions for your program.

# list to populate the inbox function
sample_emails =  [
    ['juleiga.regal@gmail.com', 'Welcome To HyperionDev', 'Python for Data Science', False],
    ['juleiga.regal_2_@gmail.com', 'Great Work on bootcamp', 'Cool stuff you can do with Python', False],
    ['juleiga.regal_3_@gmail.com', 'Great Marks', 'Machine Learning for Beginners', False]
    ]

  # Create 3 sample emails and add them to the inbox list.
def populate_inbox():
    inbox = []
    for idx, (x, y, z, p) in enumerate(sample_emails):
        emails = Email(x, y, z, p)  # do not overwrite idx
        inbox.append(emails)        # store the object itself

    return inbox
 
    pass


#inboxes = populate_inbox()
#print(inboxes[0])
#selected_email = inboxes[0]
#print(selected_email.email_address)
#print(selected_email.subject_line)
#print(selected_email.email_content)

# Mark it as read
#selected_email.mark_as_read()
#print(selected_email.has_been_read)  # Should now be True


def list_emails():
    email_list =[]
    for i, email in enumerate(inbox):
        email_list.append((i,email.subject_line))
    return email_list
    # Create a function that prints each email's subject line
    # alongside its corresponding index number,
    # regardless of whether the email has been read.
    pass


def read_email(index):
    email = inbox[index]      # this is now an Email object
    print(email.email_address)
    print(email.subject_line)
    print(email.email_content)
    email.mark_as_read()      # changes has_been_read to True

        
       
    # Create a function that displays the email_address, subject_line,
    # and email_content attributes for the selected email.
    # After displaying these details, use the 'mark_as_read()' method
    # to set its 'has_been_read' instance variable to True.
    pass



def view_unread_emails(index):
    # Create a function that displays all unread Email object subject lines
    # along with their corresponding index numbers.
    # The list of displayed emails should update as emails are read.
    email = inbox[index]
    print(email.email_address)
    print(email.has_been_read)
    pass


# --- Lists --- #
inbox = populate_inbox()

# Initialise an empty list outside the class to store the email objects.

# --- Email Program --- #

# Call the function to populate the inbox for further use in your program.

# Fill in the logic for the various menu operations.

# Display the menu options for each iteration of the loop.
while True:
    user_choice = int(
        input(
            """\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: """
        )
    )

    if user_choice == 1:
        # Show email list
        emails = list_emails()
        for i, subject in emails:
            print(f"{i}: {subject}")
        index = int(input("Enter the index of the email to read: "))
        read_email(index)

    elif user_choice == 2:
        emails = list_emails()
        for i, read_or_not in emails:
            print(f"{i}: {read_or_not}")
        index = int(input("Enter the index of the unread email: "))
        view_unread_emails(index)
        pass

    elif user_choice == 3:
        # Add logic here to quit application.
        print("Goodbye")
        break
        pass

    else:
        print("Oops - incorrect input.")
