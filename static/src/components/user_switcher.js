/** @odoo-module **/

import { Dropdown } from "@web/core/dropdown/dropdown";
import { DropdownItem } from "@web/core/dropdown/dropdown_item";
import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";

import { Component, onWillStart } from "@odoo/owl";


export class UserSwithcerMenu extends Component {
    setup() {
        this.orm = useService("orm");
        this.user = useService("user");
        onWillStart(async () => {
            this.users = await this.orm.searchRead(
                'res.users', [['id', 'not in', [this.user.userId]]], ['name', 'login']);
        });
    }

    switchUser(id) {
        window.location = '/web/switch-user?user_id=' + id;
    }

    getAvatar(id) {
        const { origin } = browser.location;
        return `${origin}/web/image?model=res.users&field=avatar_128&id=${id}`;
    }
}
UserSwithcerMenu.template = "login_as_other.UserSwitcher";
UserSwithcerMenu.components = { Dropdown, DropdownItem };

export const systrayItem = {
    Component: UserSwithcerMenu,
};
registry.category("systray").add("web.user_switcher", systrayItem, { sequence: -1 });
