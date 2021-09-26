import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                group_list.append(Group(id=str(id), name=name.strip(), header=header, footer=footer))
        finally:
            cursor.close()
        return(group_list)

    def get_contact_list(self):
        contact_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, work, mobile, phone2, email, email2, email3 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, work, mobile, phone2, email, email2, email3) = row
                contact_list.append(Contact(id=str(id),
                                            firstname=" ".join(firstname.split()),
                                            lastname=" ".join(lastname.split()),
                                            address=" ".join(address.split()),
                                            home=" ".join(home.split()),
                                            work=" ".join(work.split()),
                                            mobile=" ".join(mobile.split()),
                                            phone2=" ".join(phone2.split()),
                                            email=" ".join(email.split()),
                                            email2=" ".join(email2.split()),
                                            email3=" ".join(email3.split())))
        finally:
            cursor.close()
        return(contact_list)

    def check_relation(self, group, contact):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id from address_in_groups where id=" + str(contact.id) + " and group_id=" + str(group.id))
            row = cursor.fetchall()
            out = True if len(row) > 0 else False
        except:
            out = False
        finally:
            cursor.close()
        return(out)


    def add_relation(self, group, contact):
        cursor = self.connection.cursor()
        cursor.execute("insert into address_in_groups (id, group_id, created, deprecated) values (" + str(contact.id) + ", " + str(group.id) + ", now(), '0000-00-00 00:00:00')")
        cursor.close()


    def del_relation(self, group, contact):
        cursor = self.connection.cursor()
        cursor.execute("delete from address_in_groups where id=" + str(contact.id) + " and group_id=" + str(group.group_id))
        cursor.close()

    def destroy(self):
        self.connection.close()