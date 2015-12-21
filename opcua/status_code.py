# -*- coding: utf-8 -*-

#AUTOGENERATED!!!


class StatusCodes(object):
    Good = 0
    Uncertain = 0x40000000
    Bad = 0x80000000
    BadUnexpectedError = 0x80010000
    BadInternalError = 0x80020000
    BadOutOfMemory = 0x80030000
    BadResourceUnavailable = 0x80040000
    BadCommunicationError = 0x80050000
    BadEncodingError = 0x80060000
    BadDecodingError = 0x80070000
    BadEncodingLimitsExceeded = 0x80080000
    BadRequestTooLarge = 0x80B80000
    BadResponseTooLarge = 0x80B90000
    BadUnknownResponse = 0x80090000
    BadTimeout = 0x800A0000
    BadServiceUnsupported = 0x800B0000
    BadShutdown = 0x800C0000
    BadServerNotConnected = 0x800D0000
    BadServerHalted = 0x800E0000
    BadNothingToDo = 0x800F0000
    BadTooManyOperations = 0x80100000
    BadTooManyMonitoredItems = 0x80DB0000
    BadDataTypeIdUnknown = 0x80110000
    BadCertificateInvalid = 0x80120000
    BadSecurityChecksFailed = 0x80130000
    BadCertificateTimeInvalid = 0x80140000
    BadCertificateIssuerTimeInvalid = 0x80150000
    BadCertificateHostNameInvalid = 0x80160000
    BadCertificateUriInvalid = 0x80170000
    BadCertificateUseNotAllowed = 0x80180000
    BadCertificateIssuerUseNotAllowed = 0x80190000
    BadCertificateUntrusted = 0x801A0000
    BadCertificateRevocationUnknown = 0x801B0000
    BadCertificateIssuerRevocationUnknown = 0x801C0000
    BadCertificateRevoked = 0x801D0000
    BadCertificateIssuerRevoked = 0x801E0000
    BadCertificateChainIncomplete = 0x810D0000
    BadUserAccessDenied = 0x801F0000
    BadIdentityTokenInvalid = 0x80200000
    BadIdentityTokenRejected = 0x80210000
    BadSecureChannelIdInvalid = 0x80220000
    BadInvalidTimestamp = 0x80230000
    BadNonceInvalid = 0x80240000
    BadSessionIdInvalid = 0x80250000
    BadSessionClosed = 0x80260000
    BadSessionNotActivated = 0x80270000
    BadSubscriptionIdInvalid = 0x80280000
    BadRequestHeaderInvalid = 0x802A0000
    BadTimestampsToReturnInvalid = 0x802B0000
    BadRequestCancelledByClient = 0x802C0000
    BadTooManyArguments = 0x80E50000
    GoodSubscriptionTransferred = 0x002D0000
    GoodCompletesAsynchronously = 0x002E0000
    GoodOverload = 0x002F0000
    GoodClamped = 0x00300000
    BadNoCommunication = 0x80310000
    BadWaitingForInitialData = 0x80320000
    BadNodeIdInvalid = 0x80330000
    BadNodeIdUnknown = 0x80340000
    BadAttributeIdInvalid = 0x80350000
    BadIndexRangeInvalid = 0x80360000
    BadIndexRangeNoData = 0x80370000
    BadDataEncodingInvalid = 0x80380000
    BadDataEncodingUnsupported = 0x80390000
    BadNotReadable = 0x803A0000
    BadNotWritable = 0x803B0000
    BadOutOfRange = 0x803C0000
    BadNotSupported = 0x803D0000
    BadNotFound = 0x803E0000
    BadObjectDeleted = 0x803F0000
    BadNotImplemented = 0x80400000
    BadMonitoringModeInvalid = 0x80410000
    BadMonitoredItemIdInvalid = 0x80420000
    BadMonitoredItemFilterInvalid = 0x80430000
    BadMonitoredItemFilterUnsupported = 0x80440000
    BadFilterNotAllowed = 0x80450000
    BadStructureMissing = 0x80460000
    BadEventFilterInvalid = 0x80470000
    BadContentFilterInvalid = 0x80480000
    BadFilterOperatorInvalid = 0x80C10000
    BadFilterOperatorUnsupported = 0x80C20000
    BadFilterOperandCountMismatch = 0x80C30000
    BadFilterOperandInvalid = 0x80490000
    BadFilterElementInvalid = 0x80C40000
    BadFilterLiteralInvalid = 0x80C50000
    BadContinuationPointInvalid = 0x804A0000
    BadNoContinuationPoints = 0x804B0000
    BadReferenceTypeIdInvalid = 0x804C0000
    BadBrowseDirectionInvalid = 0x804D0000
    BadNodeNotInView = 0x804E0000
    BadServerUriInvalid = 0x804F0000
    BadServerNameMissing = 0x80500000
    BadDiscoveryUrlMissing = 0x80510000
    BadSempahoreFileMissing = 0x80520000
    BadRequestTypeInvalid = 0x80530000
    BadSecurityModeRejected = 0x80540000
    BadSecurityPolicyRejected = 0x80550000
    BadTooManySessions = 0x80560000
    BadUserSignatureInvalid = 0x80570000
    BadApplicationSignatureInvalid = 0x80580000
    BadNoValidCertificates = 0x80590000
    BadIdentityChangeNotSupported = 0x80C60000
    BadRequestCancelledByRequest = 0x805A0000
    BadParentNodeIdInvalid = 0x805B0000
    BadReferenceNotAllowed = 0x805C0000
    BadNodeIdRejected = 0x805D0000
    BadNodeIdExists = 0x805E0000
    BadNodeClassInvalid = 0x805F0000
    BadBrowseNameInvalid = 0x80600000
    BadBrowseNameDuplicated = 0x80610000
    BadNodeAttributesInvalid = 0x80620000
    BadTypeDefinitionInvalid = 0x80630000
    BadSourceNodeIdInvalid = 0x80640000
    BadTargetNodeIdInvalid = 0x80650000
    BadDuplicateReferenceNotAllowed = 0x80660000
    BadInvalidSelfReference = 0x80670000
    BadReferenceLocalOnly = 0x80680000
    BadNoDeleteRights = 0x80690000
    UncertainReferenceNotDeleted = 0x40BC0000
    BadServerIndexInvalid = 0x806A0000
    BadViewIdUnknown = 0x806B0000
    BadViewTimestampInvalid = 0x80C90000
    BadViewParameterMismatch = 0x80CA0000
    BadViewVersionInvalid = 0x80CB0000
    UncertainNotAllNodesAvailable = 0x40C00000
    GoodResultsMayBeIncomplete = 0x00BA0000
    BadNotTypeDefinition = 0x80C80000
    UncertainReferenceOutOfServer = 0x406C0000
    BadTooManyMatches = 0x806D0000
    BadQueryTooComplex = 0x806E0000
    BadNoMatch = 0x806F0000
    BadMaxAgeInvalid = 0x80700000
    BadSecurityModeInsufficient = 0x80E60000
    BadHistoryOperationInvalid = 0x80710000
    BadHistoryOperationUnsupported = 0x80720000
    BadInvalidTimestampArgument = 0x80BD0000
    BadWriteNotSupported = 0x80730000
    BadTypeMismatch = 0x80740000
    BadMethodInvalid = 0x80750000
    BadArgumentsMissing = 0x80760000
    BadTooManySubscriptions = 0x80770000
    BadTooManyPublishRequests = 0x80780000
    BadNoSubscription = 0x80790000
    BadSequenceNumberUnknown = 0x807A0000
    BadMessageNotAvailable = 0x807B0000
    BadInsufficientClientProfile = 0x807C0000
    BadStateNotActive = 0x80BF0000
    BadTcpServerTooBusy = 0x807D0000
    BadTcpMessageTypeInvalid = 0x807E0000
    BadTcpSecureChannelUnknown = 0x807F0000
    BadTcpMessageTooLarge = 0x80800000
    BadTcpNotEnoughResources = 0x80810000
    BadTcpInternalError = 0x80820000
    BadTcpEndpointUrlInvalid = 0x80830000
    BadRequestInterrupted = 0x80840000
    BadRequestTimeout = 0x80850000
    BadSecureChannelClosed = 0x80860000
    BadSecureChannelTokenUnknown = 0x80870000
    BadSequenceNumberInvalid = 0x80880000
    BadProtocolVersionUnsupported = 0x80BE0000
    BadConfigurationError = 0x80890000
    BadNotConnected = 0x808A0000
    BadDeviceFailure = 0x808B0000
    BadSensorFailure = 0x808C0000
    BadOutOfService = 0x808D0000
    BadDeadbandFilterInvalid = 0x808E0000
    UncertainNoCommunicationLastUsableValue = 0x408F0000
    UncertainLastUsableValue = 0x40900000
    UncertainSubstituteValue = 0x40910000
    UncertainInitialValue = 0x40920000
    UncertainSensorNotAccurate = 0x40930000
    UncertainEngineeringUnitsExceeded = 0x40940000
    UncertainSubNormal = 0x40950000
    GoodLocalOverride = 0x00960000
    BadRefreshInProgress = 0x80970000
    BadConditionAlreadyDisabled = 0x80980000
    BadConditionAlreadyEnabled = 0x80CC0000
    BadConditionDisabled = 0x80990000
    BadEventIdUnknown = 0x809A0000
    BadEventNotAcknowledgeable = 0x80BB0000
    BadDialogNotActive = 0x80CD0000
    BadDialogResponseInvalid = 0x80CE0000
    BadConditionBranchAlreadyAcked = 0x80CF0000
    BadConditionBranchAlreadyConfirmed = 0x80D00000
    BadConditionAlreadyShelved = 0x80D10000
    BadConditionNotShelved = 0x80D20000
    BadShelvingTimeOutOfRange = 0x80D30000
    BadNoData = 0x809B0000
    BadBoundNotFound = 0x80D70000
    BadBoundNotSupported = 0x80D80000
    BadDataLost = 0x809D0000
    BadDataUnavailable = 0x809E0000
    BadEntryExists = 0x809F0000
    BadNoEntryExists = 0x80A00000
    BadTimestampNotSupported = 0x80A10000
    GoodEntryInserted = 0x00A20000
    GoodEntryReplaced = 0x00A30000
    UncertainDataSubNormal = 0x40A40000
    GoodNoData = 0x00A50000
    GoodMoreData = 0x00A60000
    BadAggregateListMismatch = 0x80D40000
    BadAggregateNotSupported = 0x80D50000
    BadAggregateInvalidInputs = 0x80D60000
    BadAggregateConfigurationRejected = 0x80DA0000
    GoodDataIgnored = 0x00D90000
    BadRequestNotAllowed = 0x80E40000
    GoodEdited = 0x00DC0000
    GoodPostActionFailed = 0x00DD0000
    UncertainDominantValueChanged = 0x40DE0000
    GoodDependentValueChanged = 0x00E00000
    BadDominantValueChanged = 0x80E10000
    UncertainDependentValueChanged = 0x40E20000
    BadDependentValueChanged = 0x80E30000
    GoodCommunicationEvent = 0x00A70000
    GoodShutdownEvent = 0x00A80000
    GoodCallAgain = 0x00A90000
    GoodNonCriticalTimeout = 0x00AA0000
    BadInvalidArgument = 0x80AB0000
    BadConnectionRejected = 0x80AC0000
    BadDisconnect = 0x80AD0000
    BadConnectionClosed = 0x80AE0000
    BadInvalidState = 0x80AF0000
    BadEndOfStream = 0x80B00000
    BadNoDataAvailable = 0x80B10000
    BadWaitingForResponse = 0x80B20000
    BadOperationAbandoned = 0x80B30000
    BadExpectedStreamToBlock = 0x80B40000
    BadWouldBlock = 0x80B50000
    BadSyntaxError = 0x80B60000
    BadMaxConnectionsReached = 0x80B70000


code_to_name_doc = {
    0: ('Good', 'The operation completed successfully.'),
    0x40000000: ('Uncertain', 'The operation completed however its outputs may not be usable.'),
    0x80000000: ('Bad', 'The operation failed.'),
    0x80010000: ('BadUnexpectedError', 'An unexpected error occurred.'),
    0x80020000: ('BadInternalError', 'An internal error occurred as a result of a programming or configuration error.'),
    0x80030000: ('BadOutOfMemory', 'Not enough memory to complete the operation.'),
    0x80040000: ('BadResourceUnavailable', 'An operating system resource is not available.'),
    0x80050000: ('BadCommunicationError', 'A low level communication error occurred.'),
    0x80060000: ('BadEncodingError', 'Encoding halted because of invalid data in the objects being serialized.'),
    0x80070000: ('BadDecodingError', 'Decoding halted because of invalid data in the stream.'),
    0x80080000: ('BadEncodingLimitsExceeded', 'The message encoding/decoding limits imposed by the stack have been exceeded.'),
    0x80B80000: ('BadRequestTooLarge', 'The request message size exceeds limits set by the server.'),
    0x80B90000: ('BadResponseTooLarge', 'The response message size exceeds limits set by the client.'),
    0x80090000: ('BadUnknownResponse', 'An unrecognized response was received from the server.'),
    0x800A0000: ('BadTimeout', 'The operation timed out.'),
    0x800B0000: ('BadServiceUnsupported', 'The server does not support the requested service.'),
    0x800C0000: ('BadShutdown', 'The operation was cancelled because the application is shutting down.'),
    0x800D0000: ('BadServerNotConnected', 'The operation could not complete because the client is not connected to the server.'),
    0x800E0000: ('BadServerHalted', 'The server has stopped and cannot process any requests.'),
    0x800F0000: ('BadNothingToDo', 'There was nothing to do because the client passed a list of operations with no elements.'),
    0x80100000: ('BadTooManyOperations', 'The request could not be processed because it specified too many operations.'),
    0x80DB0000: ('BadTooManyMonitoredItems', 'The request could not be processed because there are too many monitored items in the subscription.'),
    0x80110000: ('BadDataTypeIdUnknown', 'The extension object cannot be (de)serialized because the data type id is not recognized.'),
    0x80120000: ('BadCertificateInvalid', 'The certificate provided as a parameter is not valid.'),
    0x80130000: ('BadSecurityChecksFailed', 'An error occurred verifying security.'),
    0x80140000: ('BadCertificateTimeInvalid', 'The Certificate has expired or is not yet valid.'),
    0x80150000: ('BadCertificateIssuerTimeInvalid', 'An Issuer Certificate has expired or is not yet valid.'),
    0x80160000: ('BadCertificateHostNameInvalid', 'The HostName used to connect to a Server does not match a HostName in the Certificate.'),
    0x80170000: ('BadCertificateUriInvalid', 'The URI specified in the ApplicationDescription does not match the URI in the Certificate.'),
    0x80180000: ('BadCertificateUseNotAllowed', 'The Certificate may not be used for the requested operation.'),
    0x80190000: ('BadCertificateIssuerUseNotAllowed', 'The Issuer Certificate may not be used for the requested operation.'),
    0x801A0000: ('BadCertificateUntrusted', 'The Certificate is not trusted.'),
    0x801B0000: ('BadCertificateRevocationUnknown', 'It was not possible to determine if the Certificate has been revoked.'),
    0x801C0000: ('BadCertificateIssuerRevocationUnknown', 'It was not possible to determine if the Issuer Certificate has been revoked.'),
    0x801D0000: ('BadCertificateRevoked', 'The certificate has been revoked.'),
    0x801E0000: ('BadCertificateIssuerRevoked', 'The issuer certificate has been revoked.'),
    0x810D0000: ('BadCertificateChainIncomplete', 'The certificate chain is incomplete.'),
    0x801F0000: ('BadUserAccessDenied', 'User does not have permission to perform the requested operation.'),
    0x80200000: ('BadIdentityTokenInvalid', 'The user identity token is not valid.'),
    0x80210000: ('BadIdentityTokenRejected', 'The user identity token is valid but the server has rejected it.'),
    0x80220000: ('BadSecureChannelIdInvalid', 'The specified secure channel is no longer valid.'),
    0x80230000: ('BadInvalidTimestamp', 'The timestamp is outside the range allowed by the server.'),
    0x80240000: ('BadNonceInvalid', 'The nonce does appear to be not a random value or it is not the correct length.'),
    0x80250000: ('BadSessionIdInvalid', 'The session id is not valid.'),
    0x80260000: ('BadSessionClosed', 'The session was closed by the client.'),
    0x80270000: ('BadSessionNotActivated', 'The session cannot be used because ActivateSession has not been called.'),
    0x80280000: ('BadSubscriptionIdInvalid', 'The subscription id is not valid.'),
    0x802A0000: ('BadRequestHeaderInvalid', 'The header for the request is missing or invalid.'),
    0x802B0000: ('BadTimestampsToReturnInvalid', 'The timestamps to return parameter is invalid.'),
    0x802C0000: ('BadRequestCancelledByClient', 'The request was cancelled by the client.'),
    0x80E50000: ('BadTooManyArguments', 'Too many arguments were provided.'),
    0x002D0000: ('GoodSubscriptionTransferred', 'The subscription was transferred to another session.'),
    0x002E0000: ('GoodCompletesAsynchronously', 'The processing will complete asynchronously.'),
    0x002F0000: ('GoodOverload', 'Sampling has slowed down due to resource limitations.'),
    0x00300000: ('GoodClamped', 'The value written was accepted but was clamped.'),
    0x80310000: ('BadNoCommunication', 'Communication with the data source is defined, but not established, and there is no last known value available.'),
    0x80320000: ('BadWaitingForInitialData', 'Waiting for the server to obtain values from the underlying data source.'),
    0x80330000: ('BadNodeIdInvalid', 'The syntax of the node id is not valid.'),
    0x80340000: ('BadNodeIdUnknown', 'The node id refers to a node that does not exist in the server address space.'),
    0x80350000: ('BadAttributeIdInvalid', 'The attribute is not supported for the specified Node.'),
    0x80360000: ('BadIndexRangeInvalid', 'The syntax of the index range parameter is invalid.'),
    0x80370000: ('BadIndexRangeNoData', 'No data exists within the range of indexes specified.'),
    0x80380000: ('BadDataEncodingInvalid', 'The data encoding is invalid.'),
    0x80390000: ('BadDataEncodingUnsupported', 'The server does not support the requested data encoding for the node.'),
    0x803A0000: ('BadNotReadable', 'The access level does not allow reading or subscribing to the Node.'),
    0x803B0000: ('BadNotWritable', 'The access level does not allow writing to the Node.'),
    0x803C0000: ('BadOutOfRange', 'The value was out of range.'),
    0x803D0000: ('BadNotSupported', 'The requested operation is not supported.'),
    0x803E0000: ('BadNotFound', 'A requested item was not found or a search operation ended without success.'),
    0x803F0000: ('BadObjectDeleted', 'The object cannot be used because it has been deleted.'),
    0x80400000: ('BadNotImplemented', 'Requested operation is not implemented.'),
    0x80410000: ('BadMonitoringModeInvalid', 'The monitoring mode is invalid.'),
    0x80420000: ('BadMonitoredItemIdInvalid', 'The monitoring item id does not refer to a valid monitored item.'),
    0x80430000: ('BadMonitoredItemFilterInvalid', 'The monitored item filter parameter is not valid.'),
    0x80440000: ('BadMonitoredItemFilterUnsupported', 'The server does not support the requested monitored item filter.'),
    0x80450000: ('BadFilterNotAllowed', 'A monitoring filter cannot be used in combination with the attribute specified.'),
    0x80460000: ('BadStructureMissing', 'A mandatory structured parameter was missing or null.'),
    0x80470000: ('BadEventFilterInvalid', 'The event filter is not valid.'),
    0x80480000: ('BadContentFilterInvalid', 'The content filter is not valid.'),
    0x80C10000: ('BadFilterOperatorInvalid', 'An unregognized operator was provided in a filter.'),
    0x80C20000: ('BadFilterOperatorUnsupported', 'A valid operator was provided, but the server does not provide support for this filter operator.'),
    0x80C30000: ('BadFilterOperandCountMismatch', 'The number of operands provided for the filter operator was less then expected for the operand provided.'),
    0x80490000: ('BadFilterOperandInvalid', 'The operand used in a content filter is not valid.'),
    0x80C40000: ('BadFilterElementInvalid', 'The referenced element is not a valid element in the content filter.'),
    0x80C50000: ('BadFilterLiteralInvalid', 'The referenced literal is not a valid value.'),
    0x804A0000: ('BadContinuationPointInvalid', 'The continuation point provide is longer valid.'),
    0x804B0000: ('BadNoContinuationPoints', 'The operation could not be processed because all continuation points have been allocated.'),
    0x804C0000: ('BadReferenceTypeIdInvalid', 'The operation could not be processed because all continuation points have been allocated.'),
    0x804D0000: ('BadBrowseDirectionInvalid', 'The browse direction is not valid.'),
    0x804E0000: ('BadNodeNotInView', 'The node is not part of the view.'),
    0x804F0000: ('BadServerUriInvalid', 'The ServerUri is not a valid URI.'),
    0x80500000: ('BadServerNameMissing', 'No ServerName was specified.'),
    0x80510000: ('BadDiscoveryUrlMissing', 'No DiscoveryUrl was specified.'),
    0x80520000: ('BadSempahoreFileMissing', 'The semaphore file specified by the client is not valid.'),
    0x80530000: ('BadRequestTypeInvalid', 'The security token request type is not valid.'),
    0x80540000: ('BadSecurityModeRejected', 'The security mode does not meet the requirements set by the Server.'),
    0x80550000: ('BadSecurityPolicyRejected', 'The security policy does not meet the requirements set by the Server.'),
    0x80560000: ('BadTooManySessions', 'The server has reached its maximum number of sessions.'),
    0x80570000: ('BadUserSignatureInvalid', 'The user token signature is missing or invalid.'),
    0x80580000: ('BadApplicationSignatureInvalid', 'The signature generated with the client certificate is missing or invalid.'),
    0x80590000: ('BadNoValidCertificates', 'The client did not provide at least one software certificate that is valid and meets the profile requirements for the server.'),
    0x80C60000: ('BadIdentityChangeNotSupported', 'The Server does not support changing the user identity assigned to the session.'),
    0x805A0000: ('BadRequestCancelledByRequest', 'The request was cancelled by the client with the Cancel service.'),
    0x805B0000: ('BadParentNodeIdInvalid', 'The parent node id does not to refer to a valid node.'),
    0x805C0000: ('BadReferenceNotAllowed', 'The reference could not be created because it violates constraints imposed by the data model.'),
    0x805D0000: ('BadNodeIdRejected', 'The requested node id was reject because it was either invalid or server does not allow node ids to be specified by the client.'),
    0x805E0000: ('BadNodeIdExists', 'The requested node id is already used by another node.'),
    0x805F0000: ('BadNodeClassInvalid', 'The node class is not valid.'),
    0x80600000: ('BadBrowseNameInvalid', 'The browse name is invalid.'),
    0x80610000: ('BadBrowseNameDuplicated', 'The browse name is not unique among nodes that share the same relationship with the parent.'),
    0x80620000: ('BadNodeAttributesInvalid', 'The node attributes are not valid for the node class.'),
    0x80630000: ('BadTypeDefinitionInvalid', 'The type definition node id does not reference an appropriate type node.'),
    0x80640000: ('BadSourceNodeIdInvalid', 'The source node id does not reference a valid node.'),
    0x80650000: ('BadTargetNodeIdInvalid', 'The target node id does not reference a valid node.'),
    0x80660000: ('BadDuplicateReferenceNotAllowed', 'The reference type between the nodes is already defined.'),
    0x80670000: ('BadInvalidSelfReference', 'The server does not allow this type of self reference on this node.'),
    0x80680000: ('BadReferenceLocalOnly', 'The reference type is not valid for a reference to a remote server.'),
    0x80690000: ('BadNoDeleteRights', 'The server will not allow the node to be deleted.'),
    0x40BC0000: ('UncertainReferenceNotDeleted', 'The server was not able to delete all target references.'),
    0x806A0000: ('BadServerIndexInvalid', 'The server index is not valid.'),
    0x806B0000: ('BadViewIdUnknown', 'The view id does not refer to a valid view node.'),
    0x80C90000: ('BadViewTimestampInvalid', 'The view timestamp is not available or not supported.'),
    0x80CA0000: ('BadViewParameterMismatch', 'The view parameters are not consistent with each other.'),
    0x80CB0000: ('BadViewVersionInvalid', 'The view version is not available or not supported.'),
    0x40C00000: ('UncertainNotAllNodesAvailable', 'The list of references may not be complete because the underlying system is not available.'),
    0x00BA0000: ('GoodResultsMayBeIncomplete', 'The server should have followed a reference to a node in a remote server but did not. The result set may be incomplete.'),
    0x80C80000: ('BadNotTypeDefinition', 'The provided Nodeid was not a type definition nodeid.'),
    0x406C0000: ('UncertainReferenceOutOfServer', 'One of the references to follow in the relative path references to a node in the address space in another server.'),
    0x806D0000: ('BadTooManyMatches', 'The requested operation has too many matches to return.'),
    0x806E0000: ('BadQueryTooComplex', 'The requested operation requires too many resources in the server.'),
    0x806F0000: ('BadNoMatch', 'The requested operation has no match to return.'),
    0x80700000: ('BadMaxAgeInvalid', 'The max age parameter is invalid.'),
    0x80E60000: ('BadSecurityModeInsufficient', 'The operation is not permitted over the current secure channel.'),
    0x80710000: ('BadHistoryOperationInvalid', 'The history details parameter is not valid.'),
    0x80720000: ('BadHistoryOperationUnsupported', 'The server does not support the requested operation.'),
    0x80BD0000: ('BadInvalidTimestampArgument', 'The defined timestamp to return was invalid.'),
    0x80730000: ('BadWriteNotSupported', 'The server not does support writing the combination of value, status and timestamps provided.'),
    0x80740000: ('BadTypeMismatch', 'The value supplied for the attribute is not of the same type as the attribute"s value.'),
    0x80750000: ('BadMethodInvalid', 'The method id does not refer to a method for the specified object.'),
    0x80760000: ('BadArgumentsMissing', 'The client did not specify all of the input arguments for the method.'),
    0x80770000: ('BadTooManySubscriptions', 'The server has reached its  maximum number of subscriptions.'),
    0x80780000: ('BadTooManyPublishRequests', 'The server has reached the maximum number of queued publish requests.'),
    0x80790000: ('BadNoSubscription', 'There is no subscription available for this session.'),
    0x807A0000: ('BadSequenceNumberUnknown', 'The sequence number is unknown to the server.'),
    0x807B0000: ('BadMessageNotAvailable', 'The requested notification message is no longer available.'),
    0x807C0000: ('BadInsufficientClientProfile', 'The Client of the current Session does not support one or more Profiles that are necessary for the Subscription.'),
    0x80BF0000: ('BadStateNotActive', 'The sub-state machine is not currently active.'),
    0x807D0000: ('BadTcpServerTooBusy', 'The server cannot process the request because it is too busy.'),
    0x807E0000: ('BadTcpMessageTypeInvalid', 'The type of the message specified in the header invalid.'),
    0x807F0000: ('BadTcpSecureChannelUnknown', 'The SecureChannelId and/or TokenId are not currently in use.'),
    0x80800000: ('BadTcpMessageTooLarge', 'The size of the message specified in the header is too large.'),
    0x80810000: ('BadTcpNotEnoughResources', 'There are not enough resources to process the request.'),
    0x80820000: ('BadTcpInternalError', 'An internal error occurred.'),
    0x80830000: ('BadTcpEndpointUrlInvalid', 'The Server does not recognize the QueryString specified.'),
    0x80840000: ('BadRequestInterrupted', 'The request could not be sent because of a network interruption.'),
    0x80850000: ('BadRequestTimeout', 'Timeout occurred while processing the request.'),
    0x80860000: ('BadSecureChannelClosed', 'The secure channel has been closed.'),
    0x80870000: ('BadSecureChannelTokenUnknown', 'The token has expired or is not recognized.'),
    0x80880000: ('BadSequenceNumberInvalid', 'The sequence number is not valid.'),
    0x80BE0000: ('BadProtocolVersionUnsupported', 'The applications do not have compatible protocol versions.'),
    0x80890000: ('BadConfigurationError', 'There is a problem with the configuration that affects the usefulness of the value.'),
    0x808A0000: ('BadNotConnected', 'The variable should receive its value from another variable, but has never been configured to do so.'),
    0x808B0000: ('BadDeviceFailure', 'There has been a failure in the device/data source that generates the value that has affected the value.'),
    0x808C0000: ('BadSensorFailure', 'There has been a failure in the sensor from which the value is derived by the device/data source.'),
    0x808D0000: ('BadOutOfService', 'The source of the data is not operational.'),
    0x808E0000: ('BadDeadbandFilterInvalid', 'The deadband filter is not valid.'),
    0x408F0000: ('UncertainNoCommunicationLastUsableValue', 'Communication to the data source has failed. The variable value is the last value that had a good quality.'),
    0x40900000: ('UncertainLastUsableValue', 'Whatever was updating this value has stopped doing so.'),
    0x40910000: ('UncertainSubstituteValue', 'The value is an operational value that was manually overwritten.'),
    0x40920000: ('UncertainInitialValue', 'The value is an initial value for a variable that normally receives its value from another variable.'),
    0x40930000: ('UncertainSensorNotAccurate', 'The value is at one of the sensor limits.'),
    0x40940000: ('UncertainEngineeringUnitsExceeded', 'The value is outside of the range of values defined for this parameter.'),
    0x40950000: ('UncertainSubNormal', 'The value is derived from multiple sources and has less than the required number of Good sources.'),
    0x00960000: ('GoodLocalOverride', 'The value has been overridden.'),
    0x80970000: ('BadRefreshInProgress', 'This Condition refresh failed, a Condition refresh operation is already in progress.'),
    0x80980000: ('BadConditionAlreadyDisabled', 'This condition has already been disabled.'),
    0x80CC0000: ('BadConditionAlreadyEnabled', 'This condition has already been enabled.'),
    0x80990000: ('BadConditionDisabled', 'Property not available, this condition is disabled.'),
    0x809A0000: ('BadEventIdUnknown', 'The specified event id is not recognized.'),
    0x80BB0000: ('BadEventNotAcknowledgeable', 'The event cannot be acknowledged.'),
    0x80CD0000: ('BadDialogNotActive', 'The dialog condition is not active.'),
    0x80CE0000: ('BadDialogResponseInvalid', 'The response is not valid for the dialog.'),
    0x80CF0000: ('BadConditionBranchAlreadyAcked', 'The condition branch has already been acknowledged.'),
    0x80D00000: ('BadConditionBranchAlreadyConfirmed', 'The condition branch has already been confirmed.'),
    0x80D10000: ('BadConditionAlreadyShelved', 'The condition has already been shelved.'),
    0x80D20000: ('BadConditionNotShelved', 'The condition is not currently shelved.'),
    0x80D30000: ('BadShelvingTimeOutOfRange', 'The shelving time not within an acceptable range.'),
    0x809B0000: ('BadNoData', 'No data exists for the requested time range or event filter.'),
    0x80D70000: ('BadBoundNotFound', 'No data found to provide upper or lower bound value.'),
    0x80D80000: ('BadBoundNotSupported', 'The server cannot retrieve a bound for the variable.'),
    0x809D0000: ('BadDataLost', 'Data is missing due to collection started/stopped/lost.'),
    0x809E0000: ('BadDataUnavailable', 'Expected data is unavailable for the requested time range due to an un-mounted volume, an off-line archive or tape, or similar reason for temporary unavailability.'),
    0x809F0000: ('BadEntryExists', 'The data or event was not successfully inserted because a matching entry exists.'),
    0x80A00000: ('BadNoEntryExists', 'The data or event was not successfully updated because no matching entry exists.'),
    0x80A10000: ('BadTimestampNotSupported', 'The client requested history using a timestamp format the server does not support (i.e requested ServerTimestamp when server only supports SourceTimestamp).'),
    0x00A20000: ('GoodEntryInserted', 'The data or event was successfully inserted into the historical database.'),
    0x00A30000: ('GoodEntryReplaced', 'The data or event field was successfully replaced in the historical database.'),
    0x40A40000: ('UncertainDataSubNormal', 'The value is derived from multiple values and has less than the required number of Good values.'),
    0x00A50000: ('GoodNoData', 'No data exists for the requested time range or event filter.'),
    0x00A60000: ('GoodMoreData', 'The data or event field was successfully replaced in the historical database.'),
    0x80D40000: ('BadAggregateListMismatch', 'The requested number of Aggregates does not match the requested number of NodeIds.'),
    0x80D50000: ('BadAggregateNotSupported', 'The requested Aggregate is not support by the server.'),
    0x80D60000: ('BadAggregateInvalidInputs', 'The aggregate value could not be derived due to invalid data inputs.'),
    0x80DA0000: ('BadAggregateConfigurationRejected', 'The aggregate configuration is not valid for specified node.'),
    0x00D90000: ('GoodDataIgnored', 'The request pecifies fields which are not valid for the EventType or cannot be saved by the historian.'),
    0x80E40000: ('BadRequestNotAllowed', 'The request was rejected by the server because it did not meet the criteria set by the server.'),
    0x00DC0000: ('GoodEdited', 'The value does not come from the real source and has been edited by the server.'),
    0x00DD0000: ('GoodPostActionFailed', 'There was an error in execution of these post-actions.'),
    0x40DE0000: ('UncertainDominantValueChanged', 'The related EngineeringUnit has been changed but the Variable Value is still provided based on the previous unit.'),
    0x00E00000: ('GoodDependentValueChanged', 'A dependent value has been changed but the change has not been applied to the device.'),
    0x80E10000: ('BadDominantValueChanged', 'The related EngineeringUnit has been changed but this change has not been applied to the device. The Variable Value is still dependent on the previous unit but its status is currently Bad.'),
    0x40E20000: ('UncertainDependentValueChanged', 'A dependent value has been changed but the change has not been applied to the device. The quality of the dominant variable is uncertain.'),
    0x80E30000: ('BadDependentValueChanged', 'A dependent value has been changed but the change has not been applied to the device. The quality of the dominant variable is Bad.'),
    0x00A70000: ('GoodCommunicationEvent', 'The communication layer has raised an event.'),
    0x00A80000: ('GoodShutdownEvent', 'The system is shutting down.'),
    0x00A90000: ('GoodCallAgain', 'The operation is not finished and needs to be called again.'),
    0x00AA0000: ('GoodNonCriticalTimeout', 'A non-critical timeout occurred.'),
    0x80AB0000: ('BadInvalidArgument', 'One or more arguments are invalid.'),
    0x80AC0000: ('BadConnectionRejected', 'Could not establish a network connection to remote server.'),
    0x80AD0000: ('BadDisconnect', 'The server has disconnected from the client.'),
    0x80AE0000: ('BadConnectionClosed', 'The network connection has been closed.'),
    0x80AF0000: ('BadInvalidState', 'The operation cannot be completed because the object is closed, uninitialized or in some other invalid state.'),
    0x80B00000: ('BadEndOfStream', 'Cannot move beyond end of the stream.'),
    0x80B10000: ('BadNoDataAvailable', 'No data is currently available for reading from a non-blocking stream.'),
    0x80B20000: ('BadWaitingForResponse', 'The asynchronous operation is waiting for a response.'),
    0x80B30000: ('BadOperationAbandoned', 'The asynchronous operation was abandoned by the caller.'),
    0x80B40000: ('BadExpectedStreamToBlock', 'The stream did not return all data requested (possibly because it is a non-blocking stream).'),
    0x80B50000: ('BadWouldBlock', 'Non blocking behaviour is required and the operation would block.'),
    0x80B60000: ('BadSyntaxError', 'A value had an invalid syntax.'),
    0x80B70000: ('BadMaxConnectionsReached', 'The operation could not be finished because all available connections are in use.'),
}


def get_name_and_doc(val):
    if val in code_to_name_doc:
        return code_to_name_doc[val]
    else:
        return 'UnknownUaError', 'Unknown StatusCode value: {}'.format(val)
