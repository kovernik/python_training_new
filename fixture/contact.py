from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.return_home()
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_home()
        self.contact_cache = None

    def return_home(self):
        wd = self.app.wd
        if not (wd.current_url == "http://localhost/addressbook/" and len(
                wd.find_elements_by_xpath("//input[@value='Delete']"))):
            wd.find_element_by_link_text("home").click()

    def edit_first_contact(self):
        wd = self.app.wd
        self.select_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.return_home()
        self.select_contact_by_index(index)
        wd.find_elements_by_css_selector('img[alt="Edit"]')[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.return_home()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nickname)
        self.change_contact_value("middlename", contact.middle)
        self.change_contact_value("address", contact.address)
        self.change_contact_value("company", contact.company)
        self.change_contact_value("home", contact.homephone)
        self.change_contact_value("mobile", contact.mobilephone)
        self.change_contact_value("email", contact.email)

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_first_contact(self):
        wd = self.app.wd
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.return_home()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.return_home()
        self.contact_cache = None

    def count (self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector("tr[name=entry]"):
                cells = element.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname))
        return list(self.contact_cache)
