"""Dell Unisphere API Models.

This module provides Pydantic models for Dell Unisphere API responses.
"""

from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class UpgradeStatusEnum(str, Enum):
    """Upgrade status enum."""

    UNKNOWN = "Unknown"
    PREPARING = "Preparing"
    PREPARED = "Prepared"
    UPGRADING = "Upgrading"
    UPGRADED = "Upgraded"
    COMMITTING = "Committing"
    COMMITTED = "Committed"
    COMPLETED = "Completed"
    FAILED = "Failed"
    ROLLING_BACK = "RollingBack"
    ROLLED_BACK = "RolledBack"


class UpgradeSessionTypeEnum(str, Enum):
    """Upgrade session type enum."""

    UNKNOWN = "Unknown"
    UPGRADE = "Upgrade"
    ROLLBACK = "Rollback"


class UpgradeTypeEnum(str, Enum):
    """Upgrade type enum."""

    UNKNOWN = "Unknown"
    FIRMWARE = "Firmware"
    SOFTWARE = "Software"
    LANGUAGE_PACK = "LanguagePack"


class Link(BaseModel):
    """API link model."""

    rel: str
    href: str


class ApiResponse(BaseModel):
    """Base API response model."""

    base: str = Field(alias="@base")
    updated: datetime
    links: List[Link]


class NameValuePair(BaseModel):
    """Name-value pair model."""

    name: str
    value: str


class FirmwarePackage(BaseModel):
    """Firmware package model."""

    name: str
    version: str


class InstalledSoftwareVersionLanguage(BaseModel):
    """Installed software version language model."""

    name: str
    version: str


class InstalledSoftwareVersionPackage(BaseModel):
    """Installed software version package model."""

    name: str
    version: str


class BasicSystemInfo(BaseModel):
    """Basic system info model."""

    id: str
    model: str
    name: str
    softwareVersion: str
    softwareFullVersion: str
    apiVersion: str
    earliestApiVersion: str


class BasicSystemInfoEntry(BaseModel):
    """Basic system info entry model."""

    content: BasicSystemInfo


class BasicSystemInfoResponse(ApiResponse):
    """Basic system info response model."""

    entries: List[BasicSystemInfoEntry]


class InstalledSoftwareVersion(BaseModel):
    """Installed software version model."""

    id: str
    version: str
    fullVersion: str
    isLatest: bool
    releaseDate: datetime
    firmwarePackages: List[FirmwarePackage] = []
    languages: List[InstalledSoftwareVersionLanguage] = []
    packages: List[InstalledSoftwareVersionPackage] = []


class InstalledSoftwareVersionEntry(BaseModel):
    """Installed software version entry model."""

    content: InstalledSoftwareVersion


class InstalledSoftwareVersionResponse(ApiResponse):
    """Installed software version response model."""

    entries: List[InstalledSoftwareVersionEntry]


class CandidateSoftwareVersion(BaseModel):
    """Candidate software version model."""

    id: str
    version: str
    fullVersion: str
    status: str
    type: UpgradeTypeEnum
    isCompatible: bool
    isValid: bool
    fileName: str
    fileSize: int
    uploadTime: datetime
    attributes: List[NameValuePair] = []


class CandidateSoftwareVersionEntry(BaseModel):
    """Candidate software version entry model."""

    content: CandidateSoftwareVersion


class CandidateSoftwareVersionResponse(ApiResponse):
    """Candidate software version response model."""

    entries: List[CandidateSoftwareVersionEntry]


class UpgradeMessage(BaseModel):
    """Upgrade message model."""

    id: str
    severity: str
    message: str
    timestamp: datetime


class UpgradeTask(BaseModel):
    """Upgrade task model."""

    id: str
    caption: str
    creationTime: datetime
    status: UpgradeStatusEnum
    type: UpgradeSessionTypeEnum
    estRemainTime: Optional[str] = None


class SoftwareUpgradeSession(BaseModel):
    """Software upgrade session model."""

    id: str
    description: Optional[str] = None
    status: UpgradeStatusEnum
    type: UpgradeSessionTypeEnum
    upgradeType: UpgradeTypeEnum
    candidateVersionId: str
    candidateVersion: str
    percentComplete: int
    startTime: datetime
    endTime: Optional[datetime] = None
    estRemainTime: Optional[str] = None
    messages: List[UpgradeMessage] = []
    tasks: List[UpgradeTask] = []


class SoftwareUpgradeSessionEntry(BaseModel):
    """Software upgrade session entry model."""

    content: SoftwareUpgradeSession


class SoftwareUpgradeSessionResponse(ApiResponse):
    """Software upgrade session response model."""

    entries: List[SoftwareUpgradeSessionEntry]
