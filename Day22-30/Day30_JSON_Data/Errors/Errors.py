# # with open ("a_file.txt") as file:
#     # file.read()

# try:
#     file=open ("a_file.txt")
#     a_dictionary={"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open ("a_file.txt","w")
#     file.write("something")
# except KeyError as errormessage:
#     print(f"The key {errormessage} does not exist")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise Key
#     # file.close()
#     # print("File was close.")
