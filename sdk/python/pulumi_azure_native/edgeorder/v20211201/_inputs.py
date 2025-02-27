# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AddressDetailsArgs',
    'AddressPropertiesArgs',
    'ConfigurationFilters',
    'ContactDetailsArgs',
    'CustomerSubscriptionDetails',
    'CustomerSubscriptionRegisteredFeatures',
    'EncryptionPreferencesArgs',
    'FilterableProperty',
    'HierarchyInformation',
    'HierarchyInformationArgs',
    'ManagementResourcePreferencesArgs',
    'NotificationPreferenceArgs',
    'OrderItemDetailsArgs',
    'PreferencesArgs',
    'ProductDetailsArgs',
    'ShippingAddressArgs',
    'TransportPreferencesArgs',
]

@pulumi.input_type
class AddressDetailsArgs:
    def __init__(__self__, *,
                 forward_address: pulumi.Input['AddressPropertiesArgs']):
        """
        Address details for an order item.
        :param pulumi.Input['AddressPropertiesArgs'] forward_address: Customer address and contact details. It should be address resource
        """
        pulumi.set(__self__, "forward_address", forward_address)

    @property
    @pulumi.getter(name="forwardAddress")
    def forward_address(self) -> pulumi.Input['AddressPropertiesArgs']:
        """
        Customer address and contact details. It should be address resource
        """
        return pulumi.get(self, "forward_address")

    @forward_address.setter
    def forward_address(self, value: pulumi.Input['AddressPropertiesArgs']):
        pulumi.set(self, "forward_address", value)


@pulumi.input_type
class AddressPropertiesArgs:
    def __init__(__self__, *,
                 contact_details: pulumi.Input['ContactDetailsArgs'],
                 shipping_address: Optional[pulumi.Input['ShippingAddressArgs']] = None):
        """
        Address Properties
        :param pulumi.Input['ContactDetailsArgs'] contact_details: Contact details for the address
        :param pulumi.Input['ShippingAddressArgs'] shipping_address: Shipping details for the address
        """
        pulumi.set(__self__, "contact_details", contact_details)
        if shipping_address is not None:
            pulumi.set(__self__, "shipping_address", shipping_address)

    @property
    @pulumi.getter(name="contactDetails")
    def contact_details(self) -> pulumi.Input['ContactDetailsArgs']:
        """
        Contact details for the address
        """
        return pulumi.get(self, "contact_details")

    @contact_details.setter
    def contact_details(self, value: pulumi.Input['ContactDetailsArgs']):
        pulumi.set(self, "contact_details", value)

    @property
    @pulumi.getter(name="shippingAddress")
    def shipping_address(self) -> Optional[pulumi.Input['ShippingAddressArgs']]:
        """
        Shipping details for the address
        """
        return pulumi.get(self, "shipping_address")

    @shipping_address.setter
    def shipping_address(self, value: Optional[pulumi.Input['ShippingAddressArgs']]):
        pulumi.set(self, "shipping_address", value)


@pulumi.input_type
class ConfigurationFilters:
    def __init__(__self__, *,
                 hierarchy_information: 'HierarchyInformation',
                 filterable_property: Optional[Sequence['FilterableProperty']] = None):
        """
        Configuration filters
        :param 'HierarchyInformation' hierarchy_information: Product hierarchy information
        :param Sequence['FilterableProperty'] filterable_property: Filters specific to product
        """
        pulumi.set(__self__, "hierarchy_information", hierarchy_information)
        if filterable_property is not None:
            pulumi.set(__self__, "filterable_property", filterable_property)

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> 'HierarchyInformation':
        """
        Product hierarchy information
        """
        return pulumi.get(self, "hierarchy_information")

    @hierarchy_information.setter
    def hierarchy_information(self, value: 'HierarchyInformation'):
        pulumi.set(self, "hierarchy_information", value)

    @property
    @pulumi.getter(name="filterableProperty")
    def filterable_property(self) -> Optional[Sequence['FilterableProperty']]:
        """
        Filters specific to product
        """
        return pulumi.get(self, "filterable_property")

    @filterable_property.setter
    def filterable_property(self, value: Optional[Sequence['FilterableProperty']]):
        pulumi.set(self, "filterable_property", value)


@pulumi.input_type
class ContactDetailsArgs:
    def __init__(__self__, *,
                 contact_name: pulumi.Input[str],
                 email_list: pulumi.Input[Sequence[pulumi.Input[str]]],
                 phone: pulumi.Input[str],
                 mobile: Optional[pulumi.Input[str]] = None,
                 phone_extension: Optional[pulumi.Input[str]] = None):
        """
        Contact Details.
        :param pulumi.Input[str] contact_name: Contact name of the person.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] email_list: List of Email-ids to be notified about job progress.
        :param pulumi.Input[str] phone: Phone number of the contact person.
        :param pulumi.Input[str] mobile: Mobile number of the contact person.
        :param pulumi.Input[str] phone_extension: Phone extension number of the contact person.
        """
        pulumi.set(__self__, "contact_name", contact_name)
        pulumi.set(__self__, "email_list", email_list)
        pulumi.set(__self__, "phone", phone)
        if mobile is not None:
            pulumi.set(__self__, "mobile", mobile)
        if phone_extension is not None:
            pulumi.set(__self__, "phone_extension", phone_extension)

    @property
    @pulumi.getter(name="contactName")
    def contact_name(self) -> pulumi.Input[str]:
        """
        Contact name of the person.
        """
        return pulumi.get(self, "contact_name")

    @contact_name.setter
    def contact_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "contact_name", value)

    @property
    @pulumi.getter(name="emailList")
    def email_list(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of Email-ids to be notified about job progress.
        """
        return pulumi.get(self, "email_list")

    @email_list.setter
    def email_list(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "email_list", value)

    @property
    @pulumi.getter
    def phone(self) -> pulumi.Input[str]:
        """
        Phone number of the contact person.
        """
        return pulumi.get(self, "phone")

    @phone.setter
    def phone(self, value: pulumi.Input[str]):
        pulumi.set(self, "phone", value)

    @property
    @pulumi.getter
    def mobile(self) -> Optional[pulumi.Input[str]]:
        """
        Mobile number of the contact person.
        """
        return pulumi.get(self, "mobile")

    @mobile.setter
    def mobile(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mobile", value)

    @property
    @pulumi.getter(name="phoneExtension")
    def phone_extension(self) -> Optional[pulumi.Input[str]]:
        """
        Phone extension number of the contact person.
        """
        return pulumi.get(self, "phone_extension")

    @phone_extension.setter
    def phone_extension(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_extension", value)


@pulumi.input_type
class CustomerSubscriptionDetails:
    def __init__(__self__, *,
                 quota_id: str,
                 location_placement_id: Optional[str] = None,
                 registered_features: Optional[Sequence['CustomerSubscriptionRegisteredFeatures']] = None):
        """
        Holds Customer subscription details. Clients can display available products to unregistered customers by explicitly passing subscription details
        :param str quota_id: Quota ID of a subscription
        :param str location_placement_id: Location placement Id of a subscription
        :param Sequence['CustomerSubscriptionRegisteredFeatures'] registered_features: List of registered feature flags for subscription
        """
        pulumi.set(__self__, "quota_id", quota_id)
        if location_placement_id is not None:
            pulumi.set(__self__, "location_placement_id", location_placement_id)
        if registered_features is not None:
            pulumi.set(__self__, "registered_features", registered_features)

    @property
    @pulumi.getter(name="quotaId")
    def quota_id(self) -> str:
        """
        Quota ID of a subscription
        """
        return pulumi.get(self, "quota_id")

    @quota_id.setter
    def quota_id(self, value: str):
        pulumi.set(self, "quota_id", value)

    @property
    @pulumi.getter(name="locationPlacementId")
    def location_placement_id(self) -> Optional[str]:
        """
        Location placement Id of a subscription
        """
        return pulumi.get(self, "location_placement_id")

    @location_placement_id.setter
    def location_placement_id(self, value: Optional[str]):
        pulumi.set(self, "location_placement_id", value)

    @property
    @pulumi.getter(name="registeredFeatures")
    def registered_features(self) -> Optional[Sequence['CustomerSubscriptionRegisteredFeatures']]:
        """
        List of registered feature flags for subscription
        """
        return pulumi.get(self, "registered_features")

    @registered_features.setter
    def registered_features(self, value: Optional[Sequence['CustomerSubscriptionRegisteredFeatures']]):
        pulumi.set(self, "registered_features", value)


@pulumi.input_type
class CustomerSubscriptionRegisteredFeatures:
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 state: Optional[str] = None):
        """
        Represents subscription registered features
        :param str name: Name of subscription registered feature
        :param str state: State of subscription registered feature
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of subscription registered feature
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        State of subscription registered feature
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[str]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class EncryptionPreferencesArgs:
    def __init__(__self__, *,
                 double_encryption_status: Optional[pulumi.Input[Union[str, 'DoubleEncryptionStatus']]] = None):
        """
        Preferences related to the double encryption
        :param pulumi.Input[Union[str, 'DoubleEncryptionStatus']] double_encryption_status: Double encryption status as entered by the customer. It is compulsory to give this parameter if the 'Deny' or 'Disabled' policy is configured.
        """
        if double_encryption_status is not None:
            pulumi.set(__self__, "double_encryption_status", double_encryption_status)

    @property
    @pulumi.getter(name="doubleEncryptionStatus")
    def double_encryption_status(self) -> Optional[pulumi.Input[Union[str, 'DoubleEncryptionStatus']]]:
        """
        Double encryption status as entered by the customer. It is compulsory to give this parameter if the 'Deny' or 'Disabled' policy is configured.
        """
        return pulumi.get(self, "double_encryption_status")

    @double_encryption_status.setter
    def double_encryption_status(self, value: Optional[pulumi.Input[Union[str, 'DoubleEncryptionStatus']]]):
        pulumi.set(self, "double_encryption_status", value)


@pulumi.input_type
class FilterableProperty:
    def __init__(__self__, *,
                 supported_values: Sequence[str],
                 type: Union[str, 'SupportedFilterTypes']):
        """
        Different types of filters supported and its values.
        :param Sequence[str] supported_values: Values to be filtered.
        :param Union[str, 'SupportedFilterTypes'] type: Type of product filter.
        """
        pulumi.set(__self__, "supported_values", supported_values)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="supportedValues")
    def supported_values(self) -> Sequence[str]:
        """
        Values to be filtered.
        """
        return pulumi.get(self, "supported_values")

    @supported_values.setter
    def supported_values(self, value: Sequence[str]):
        pulumi.set(self, "supported_values", value)

    @property
    @pulumi.getter
    def type(self) -> Union[str, 'SupportedFilterTypes']:
        """
        Type of product filter.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Union[str, 'SupportedFilterTypes']):
        pulumi.set(self, "type", value)


@pulumi.input_type
class HierarchyInformation:
    def __init__(__self__, *,
                 configuration_name: Optional[str] = None,
                 product_family_name: Optional[str] = None,
                 product_line_name: Optional[str] = None,
                 product_name: Optional[str] = None):
        """
        Holds details about product hierarchy information
        :param str configuration_name: Represents configuration name that uniquely identifies configuration
        :param str product_family_name: Represents product family name that uniquely identifies product family
        :param str product_line_name: Represents product line name that uniquely identifies product line
        :param str product_name: Represents product name that uniquely identifies product
        """
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if product_family_name is not None:
            pulumi.set(__self__, "product_family_name", product_family_name)
        if product_line_name is not None:
            pulumi.set(__self__, "product_line_name", product_line_name)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[str]:
        """
        Represents configuration name that uniquely identifies configuration
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[str]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[str]:
        """
        Represents product family name that uniquely identifies product family
        """
        return pulumi.get(self, "product_family_name")

    @product_family_name.setter
    def product_family_name(self, value: Optional[str]):
        pulumi.set(self, "product_family_name", value)

    @property
    @pulumi.getter(name="productLineName")
    def product_line_name(self) -> Optional[str]:
        """
        Represents product line name that uniquely identifies product line
        """
        return pulumi.get(self, "product_line_name")

    @product_line_name.setter
    def product_line_name(self, value: Optional[str]):
        pulumi.set(self, "product_line_name", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[str]:
        """
        Represents product name that uniquely identifies product
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: Optional[str]):
        pulumi.set(self, "product_name", value)


@pulumi.input_type
class HierarchyInformationArgs:
    def __init__(__self__, *,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 product_family_name: Optional[pulumi.Input[str]] = None,
                 product_line_name: Optional[pulumi.Input[str]] = None,
                 product_name: Optional[pulumi.Input[str]] = None):
        """
        Holds details about product hierarchy information
        :param pulumi.Input[str] configuration_name: Represents configuration name that uniquely identifies configuration
        :param pulumi.Input[str] product_family_name: Represents product family name that uniquely identifies product family
        :param pulumi.Input[str] product_line_name: Represents product line name that uniquely identifies product line
        :param pulumi.Input[str] product_name: Represents product name that uniquely identifies product
        """
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if product_family_name is not None:
            pulumi.set(__self__, "product_family_name", product_family_name)
        if product_line_name is not None:
            pulumi.set(__self__, "product_line_name", product_line_name)
        if product_name is not None:
            pulumi.set(__self__, "product_name", product_name)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        Represents configuration name that uniquely identifies configuration
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter(name="productFamilyName")
    def product_family_name(self) -> Optional[pulumi.Input[str]]:
        """
        Represents product family name that uniquely identifies product family
        """
        return pulumi.get(self, "product_family_name")

    @product_family_name.setter
    def product_family_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_family_name", value)

    @property
    @pulumi.getter(name="productLineName")
    def product_line_name(self) -> Optional[pulumi.Input[str]]:
        """
        Represents product line name that uniquely identifies product line
        """
        return pulumi.get(self, "product_line_name")

    @product_line_name.setter
    def product_line_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_line_name", value)

    @property
    @pulumi.getter(name="productName")
    def product_name(self) -> Optional[pulumi.Input[str]]:
        """
        Represents product name that uniquely identifies product
        """
        return pulumi.get(self, "product_name")

    @product_name.setter
    def product_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_name", value)


@pulumi.input_type
class ManagementResourcePreferencesArgs:
    def __init__(__self__, *,
                 preferred_management_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Management resource preference to link device
        :param pulumi.Input[str] preferred_management_resource_id: Customer preferred Management resource ARM ID
        """
        if preferred_management_resource_id is not None:
            pulumi.set(__self__, "preferred_management_resource_id", preferred_management_resource_id)

    @property
    @pulumi.getter(name="preferredManagementResourceId")
    def preferred_management_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Customer preferred Management resource ARM ID
        """
        return pulumi.get(self, "preferred_management_resource_id")

    @preferred_management_resource_id.setter
    def preferred_management_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "preferred_management_resource_id", value)


@pulumi.input_type
class NotificationPreferenceArgs:
    def __init__(__self__, *,
                 send_notification: pulumi.Input[bool],
                 stage_name: pulumi.Input[Union[str, 'NotificationStageName']]):
        """
        Notification preference for a job stage.
        :param pulumi.Input[bool] send_notification: Notification is required or not.
        :param pulumi.Input[Union[str, 'NotificationStageName']] stage_name: Name of the stage.
        """
        pulumi.set(__self__, "send_notification", send_notification)
        pulumi.set(__self__, "stage_name", stage_name)

    @property
    @pulumi.getter(name="sendNotification")
    def send_notification(self) -> pulumi.Input[bool]:
        """
        Notification is required or not.
        """
        return pulumi.get(self, "send_notification")

    @send_notification.setter
    def send_notification(self, value: pulumi.Input[bool]):
        pulumi.set(self, "send_notification", value)

    @property
    @pulumi.getter(name="stageName")
    def stage_name(self) -> pulumi.Input[Union[str, 'NotificationStageName']]:
        """
        Name of the stage.
        """
        return pulumi.get(self, "stage_name")

    @stage_name.setter
    def stage_name(self, value: pulumi.Input[Union[str, 'NotificationStageName']]):
        pulumi.set(self, "stage_name", value)


@pulumi.input_type
class OrderItemDetailsArgs:
    def __init__(__self__, *,
                 order_item_type: pulumi.Input[Union[str, 'OrderItemType']],
                 product_details: pulumi.Input['ProductDetailsArgs'],
                 notification_email_list: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 preferences: Optional[pulumi.Input['PreferencesArgs']] = None):
        """
        Order item details
        :param pulumi.Input[Union[str, 'OrderItemType']] order_item_type: Order item type.
        :param pulumi.Input['ProductDetailsArgs'] product_details: Unique identifier for configuration.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] notification_email_list: Additional notification email list
        :param pulumi.Input['PreferencesArgs'] preferences: Customer notification Preferences
        """
        pulumi.set(__self__, "order_item_type", order_item_type)
        pulumi.set(__self__, "product_details", product_details)
        if notification_email_list is not None:
            pulumi.set(__self__, "notification_email_list", notification_email_list)
        if preferences is not None:
            pulumi.set(__self__, "preferences", preferences)

    @property
    @pulumi.getter(name="orderItemType")
    def order_item_type(self) -> pulumi.Input[Union[str, 'OrderItemType']]:
        """
        Order item type.
        """
        return pulumi.get(self, "order_item_type")

    @order_item_type.setter
    def order_item_type(self, value: pulumi.Input[Union[str, 'OrderItemType']]):
        pulumi.set(self, "order_item_type", value)

    @property
    @pulumi.getter(name="productDetails")
    def product_details(self) -> pulumi.Input['ProductDetailsArgs']:
        """
        Unique identifier for configuration.
        """
        return pulumi.get(self, "product_details")

    @product_details.setter
    def product_details(self, value: pulumi.Input['ProductDetailsArgs']):
        pulumi.set(self, "product_details", value)

    @property
    @pulumi.getter(name="notificationEmailList")
    def notification_email_list(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Additional notification email list
        """
        return pulumi.get(self, "notification_email_list")

    @notification_email_list.setter
    def notification_email_list(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "notification_email_list", value)

    @property
    @pulumi.getter
    def preferences(self) -> Optional[pulumi.Input['PreferencesArgs']]:
        """
        Customer notification Preferences
        """
        return pulumi.get(self, "preferences")

    @preferences.setter
    def preferences(self, value: Optional[pulumi.Input['PreferencesArgs']]):
        pulumi.set(self, "preferences", value)


@pulumi.input_type
class PreferencesArgs:
    def __init__(__self__, *,
                 encryption_preferences: Optional[pulumi.Input['EncryptionPreferencesArgs']] = None,
                 management_resource_preferences: Optional[pulumi.Input['ManagementResourcePreferencesArgs']] = None,
                 notification_preferences: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPreferenceArgs']]]] = None,
                 transport_preferences: Optional[pulumi.Input['TransportPreferencesArgs']] = None):
        """
        Preferences related to the order
        :param pulumi.Input['EncryptionPreferencesArgs'] encryption_preferences: Preferences related to the Encryption.
        :param pulumi.Input['ManagementResourcePreferencesArgs'] management_resource_preferences: Preferences related to the Management resource.
        :param pulumi.Input[Sequence[pulumi.Input['NotificationPreferenceArgs']]] notification_preferences: Notification preferences.
        :param pulumi.Input['TransportPreferencesArgs'] transport_preferences: Preferences related to the shipment logistics of the order.
        """
        if encryption_preferences is not None:
            pulumi.set(__self__, "encryption_preferences", encryption_preferences)
        if management_resource_preferences is not None:
            pulumi.set(__self__, "management_resource_preferences", management_resource_preferences)
        if notification_preferences is not None:
            pulumi.set(__self__, "notification_preferences", notification_preferences)
        if transport_preferences is not None:
            pulumi.set(__self__, "transport_preferences", transport_preferences)

    @property
    @pulumi.getter(name="encryptionPreferences")
    def encryption_preferences(self) -> Optional[pulumi.Input['EncryptionPreferencesArgs']]:
        """
        Preferences related to the Encryption.
        """
        return pulumi.get(self, "encryption_preferences")

    @encryption_preferences.setter
    def encryption_preferences(self, value: Optional[pulumi.Input['EncryptionPreferencesArgs']]):
        pulumi.set(self, "encryption_preferences", value)

    @property
    @pulumi.getter(name="managementResourcePreferences")
    def management_resource_preferences(self) -> Optional[pulumi.Input['ManagementResourcePreferencesArgs']]:
        """
        Preferences related to the Management resource.
        """
        return pulumi.get(self, "management_resource_preferences")

    @management_resource_preferences.setter
    def management_resource_preferences(self, value: Optional[pulumi.Input['ManagementResourcePreferencesArgs']]):
        pulumi.set(self, "management_resource_preferences", value)

    @property
    @pulumi.getter(name="notificationPreferences")
    def notification_preferences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPreferenceArgs']]]]:
        """
        Notification preferences.
        """
        return pulumi.get(self, "notification_preferences")

    @notification_preferences.setter
    def notification_preferences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NotificationPreferenceArgs']]]]):
        pulumi.set(self, "notification_preferences", value)

    @property
    @pulumi.getter(name="transportPreferences")
    def transport_preferences(self) -> Optional[pulumi.Input['TransportPreferencesArgs']]:
        """
        Preferences related to the shipment logistics of the order.
        """
        return pulumi.get(self, "transport_preferences")

    @transport_preferences.setter
    def transport_preferences(self, value: Optional[pulumi.Input['TransportPreferencesArgs']]):
        pulumi.set(self, "transport_preferences", value)


@pulumi.input_type
class ProductDetailsArgs:
    def __init__(__self__, *,
                 hierarchy_information: pulumi.Input['HierarchyInformationArgs']):
        """
        Represents product details
        :param pulumi.Input['HierarchyInformationArgs'] hierarchy_information: Hierarchy of the product which uniquely identifies the product
        """
        pulumi.set(__self__, "hierarchy_information", hierarchy_information)

    @property
    @pulumi.getter(name="hierarchyInformation")
    def hierarchy_information(self) -> pulumi.Input['HierarchyInformationArgs']:
        """
        Hierarchy of the product which uniquely identifies the product
        """
        return pulumi.get(self, "hierarchy_information")

    @hierarchy_information.setter
    def hierarchy_information(self, value: pulumi.Input['HierarchyInformationArgs']):
        pulumi.set(self, "hierarchy_information", value)


@pulumi.input_type
class ShippingAddressArgs:
    def __init__(__self__, *,
                 country: pulumi.Input[str],
                 street_address1: pulumi.Input[str],
                 address_type: Optional[pulumi.Input[Union[str, 'AddressType']]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 company_name: Optional[pulumi.Input[str]] = None,
                 postal_code: Optional[pulumi.Input[str]] = None,
                 state_or_province: Optional[pulumi.Input[str]] = None,
                 street_address2: Optional[pulumi.Input[str]] = None,
                 street_address3: Optional[pulumi.Input[str]] = None,
                 zip_extended_code: Optional[pulumi.Input[str]] = None):
        """
        Shipping address where customer wishes to receive the device.
        :param pulumi.Input[str] country: Name of the Country.
        :param pulumi.Input[str] street_address1: Street Address line 1.
        :param pulumi.Input[Union[str, 'AddressType']] address_type: Type of address.
        :param pulumi.Input[str] city: Name of the City.
        :param pulumi.Input[str] company_name: Name of the company.
        :param pulumi.Input[str] postal_code: Postal code.
        :param pulumi.Input[str] state_or_province: Name of the State or Province.
        :param pulumi.Input[str] street_address2: Street Address line 2.
        :param pulumi.Input[str] street_address3: Street Address line 3.
        :param pulumi.Input[str] zip_extended_code: Extended Zip Code.
        """
        pulumi.set(__self__, "country", country)
        pulumi.set(__self__, "street_address1", street_address1)
        if address_type is not None:
            pulumi.set(__self__, "address_type", address_type)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if company_name is not None:
            pulumi.set(__self__, "company_name", company_name)
        if postal_code is not None:
            pulumi.set(__self__, "postal_code", postal_code)
        if state_or_province is not None:
            pulumi.set(__self__, "state_or_province", state_or_province)
        if street_address2 is not None:
            pulumi.set(__self__, "street_address2", street_address2)
        if street_address3 is not None:
            pulumi.set(__self__, "street_address3", street_address3)
        if zip_extended_code is not None:
            pulumi.set(__self__, "zip_extended_code", zip_extended_code)

    @property
    @pulumi.getter
    def country(self) -> pulumi.Input[str]:
        """
        Name of the Country.
        """
        return pulumi.get(self, "country")

    @country.setter
    def country(self, value: pulumi.Input[str]):
        pulumi.set(self, "country", value)

    @property
    @pulumi.getter(name="streetAddress1")
    def street_address1(self) -> pulumi.Input[str]:
        """
        Street Address line 1.
        """
        return pulumi.get(self, "street_address1")

    @street_address1.setter
    def street_address1(self, value: pulumi.Input[str]):
        pulumi.set(self, "street_address1", value)

    @property
    @pulumi.getter(name="addressType")
    def address_type(self) -> Optional[pulumi.Input[Union[str, 'AddressType']]]:
        """
        Type of address.
        """
        return pulumi.get(self, "address_type")

    @address_type.setter
    def address_type(self, value: Optional[pulumi.Input[Union[str, 'AddressType']]]):
        pulumi.set(self, "address_type", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the City.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the company.
        """
        return pulumi.get(self, "company_name")

    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "company_name", value)

    @property
    @pulumi.getter(name="postalCode")
    def postal_code(self) -> Optional[pulumi.Input[str]]:
        """
        Postal code.
        """
        return pulumi.get(self, "postal_code")

    @postal_code.setter
    def postal_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "postal_code", value)

    @property
    @pulumi.getter(name="stateOrProvince")
    def state_or_province(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the State or Province.
        """
        return pulumi.get(self, "state_or_province")

    @state_or_province.setter
    def state_or_province(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state_or_province", value)

    @property
    @pulumi.getter(name="streetAddress2")
    def street_address2(self) -> Optional[pulumi.Input[str]]:
        """
        Street Address line 2.
        """
        return pulumi.get(self, "street_address2")

    @street_address2.setter
    def street_address2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "street_address2", value)

    @property
    @pulumi.getter(name="streetAddress3")
    def street_address3(self) -> Optional[pulumi.Input[str]]:
        """
        Street Address line 3.
        """
        return pulumi.get(self, "street_address3")

    @street_address3.setter
    def street_address3(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "street_address3", value)

    @property
    @pulumi.getter(name="zipExtendedCode")
    def zip_extended_code(self) -> Optional[pulumi.Input[str]]:
        """
        Extended Zip Code.
        """
        return pulumi.get(self, "zip_extended_code")

    @zip_extended_code.setter
    def zip_extended_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_extended_code", value)


@pulumi.input_type
class TransportPreferencesArgs:
    def __init__(__self__, *,
                 preferred_shipment_type: pulumi.Input[Union[str, 'TransportShipmentTypes']]):
        """
        Preferences related to the shipment logistics of the sku
        :param pulumi.Input[Union[str, 'TransportShipmentTypes']] preferred_shipment_type: Indicates Shipment Logistics type that the customer preferred.
        """
        pulumi.set(__self__, "preferred_shipment_type", preferred_shipment_type)

    @property
    @pulumi.getter(name="preferredShipmentType")
    def preferred_shipment_type(self) -> pulumi.Input[Union[str, 'TransportShipmentTypes']]:
        """
        Indicates Shipment Logistics type that the customer preferred.
        """
        return pulumi.get(self, "preferred_shipment_type")

    @preferred_shipment_type.setter
    def preferred_shipment_type(self, value: pulumi.Input[Union[str, 'TransportShipmentTypes']]):
        pulumi.set(self, "preferred_shipment_type", value)


