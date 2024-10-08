from dataall.base.api.context import Context
from dataall.core.permissions.services.tenant_policy_service import TenantPolicyService
from dataall.modules.catalog.services.glossaries_service import GlossariesService
from dataall.modules.metadata_forms.db.metadata_form_models import MetadataForm, MetadataFormField
from dataall.modules.metadata_forms.services.metadata_form_permissions import MANAGE_METADATA_FORMS
from dataall.modules.metadata_forms.services.metadata_form_service import MetadataFormService, MetadataFormAccessService


def create_metadata_form(context: Context, source, input):
    return MetadataFormService.create_metadata_form(data=input)


def delete_metadata_form(context: Context, source, formUri):
    return MetadataFormService.delete_metadata_form_by_uri(uri=formUri)


def list_metadata_forms(context: Context, source, filter=None):
    return MetadataFormService.paginated_metadata_form_list(filter=filter)


def get_home_entity_name(context: Context, source: MetadataForm):
    return MetadataFormService.get_home_entity_name(metadata_form=source)


def get_metadata_form(context: Context, source, uri):
    return MetadataFormService.get_metadata_form_by_uri(uri=uri)


def get_form_fields(context: Context, source: MetadataForm):
    return MetadataFormService.get_metadata_form_fields(uri=source.uri)


def create_metadata_form_fields(context: Context, source, formUri, input):
    return MetadataFormService.create_metadata_form_fields(uri=formUri, data_arr=input)


def delete_metadata_form_field(context: Context, source, formUri, fieldUri):
    return MetadataFormService.delete_metadata_form_field(uri=formUri, fieldUri=fieldUri)


def batch_metadata_form_field_update(context: Context, source, formUri, input):
    return MetadataFormService.batch_metadata_form_field_update(uri=formUri, data=input)


def get_user_role(context: Context, source: MetadataForm):
    return MetadataFormAccessService.get_user_role(uri=source.uri)


def get_fields_glossary_node_name(context: Context, source: MetadataFormField):
    return GlossariesService.get_node(source.glossaryNodeUri).label if source.glossaryNodeUri else None


def has_tenant_permissions_for_metadata_forms(context: Context, source: MetadataForm):
    return TenantPolicyService.has_user_tenant_permission(
        groups=context.groups,
        tenant_name=TenantPolicyService.TENANT_NAME,
        permission_name=MANAGE_METADATA_FORMS,
    )
