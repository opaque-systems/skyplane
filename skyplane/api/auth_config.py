from dataclasses import dataclass

from typing import Optional

from skyplane import compute


class AuthenticationConfig:
    def make_auth_provider(self):
        raise NotImplementedError


@dataclass
class AWSConfig(AuthenticationConfig):
    aws_access_key: Optional[str] = None
    aws_secret_key: Optional[str] = None
    aws_enabled: bool = True

    def make_auth_provider(self) -> compute.AWSAuthentication:
        return compute.AWSAuthentication(config=self)  # type: ignore


@dataclass
class AzureConfig(AuthenticationConfig):
    azure_subscription_id: str
    azure_resource_group: str
    azure_umi_id: str
    azure_umi_name: str
    azure_umi_client_id: str
    azure_enabled: bool = True

    def make_auth_provider(self) -> compute.AzureAuthentication:
        return compute.AzureAuthentication(config=self)  # type: ignore


@dataclass
class GCPConfig(AuthenticationConfig):
    gcp_project_id: str
    gcp_enabled: bool = True

    def make_auth_provider(self) -> compute.GCPAuthentication:
        return compute.GCPAuthentication(config=self)  # type: ignore

@dataclass
class IBMCloudConfig(AuthenticationConfig):
    ibmcloud_access_id: Optional[str] = None
    ibmcloud_secret_key: Optional[str] = None
    ibmcloud_api_key: Optional[str] = None
    ibmcloud_iam_key: Optional[str] = None
    ibmcloud_iam_endpoint: Optional[str] = None
    ibmcloud_useragent: Optional[str] = None
    ibmcloud_region: Optional[str] = None
    ibmcloud_enabled:bool = False

    def make_auth_provider(self) -> compute.IBMCloudAuthentication:
        return compute.IBMCloudAuthentication(config=self)  # type: ignore