import { registry } from '@web/core/registry';

function hideCreateButton(action) {
    if (action.res_model === 'digizilla.digizilla') {
        action.views = action.views.map(view => {
            if (view.type === 'form') {
                view.arch = view.arch.replace('<form', '<form create="false"');
            }
            return view;
        });
    }
}

registry.category('actions').add('hide_create_button', hideCreateButton);
