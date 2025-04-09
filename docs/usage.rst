Usage
=====

Basic Usage
----------

To enable collaborative editing for a specific admin class, inherit from the ``CollaborativeAdminMixin`` and register your model:

.. code-block:: python

    from django.contrib import admin
    from django_admin_collaborator.utils import CollaborativeAdminMixin
    from myapp.models import MyModel

    @admin.register(MyModel)
    class MyModelAdmin(CollaborativeAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'description')
        # ... your other admin configurations

Advanced Usage
------------

Applying to Multiple Admin Classes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the utility functions to apply collaborative editing to existing admin classes:

.. code-block:: python

    from django.contrib import admin
    from django_admin_collaborator.utils import make_collaborative
    from myapp.models import MyModel

    # Create your admin class
    class MyModelAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')
        # ... your other admin configurations

    # Apply collaborative editing
    CollaborativeMyModelAdmin = make_collaborative(MyModelAdmin)

    # Register with admin
    admin.site.register(MyModel, CollaborativeMyModelAdmin)

Creating Admin Classes Dynamically
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use the factory function to create admin classes dynamically:

.. code-block:: python

    from django.contrib import admin
    from django_admin_collaborator.utils import collaborative_admin_factory
    from myapp.models import MyModel

    # Create and register the admin class in one go
    admin.site.register(
        MyModel,
        collaborative_admin_factory(
            MyModel,
            admin_options={
                'list_display': ('name', 'description'),
                'search_fields': ('name',),
            }
        )
    )

Customize Info Texts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can customize the texts displayed to users in different scenarios. This is done by setting the `ADMIN_COLLABORATOR_OPTIONS` dictionary in your settings.py file.
To ensure the `{editor_name}` placeholder works correctly, it must be written exactly as `{editor_name}` in your settings. If you modify the placeholder or omit the curly braces, it will not work as expected.

.. code-block:: python

    ADMIN_COLLABORATOR_OPTIONS = {
        "editor_mode_text": "You are in editor mode.",
        "viewer_mode_text": "This page is being edited by {editor_name}. You cannot make changes until they leave.",
        "claiming_editor_text": "The editor has left. The page will refresh shortly to allow editing."
    }