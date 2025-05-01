// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "UnifiedConsentSDK",
    platforms: [
        .iOS(.v13)
    ],
    products: [
        .library(
            name: "UnifiedConsentSDK",
            targets: ["UnifiedConsentSDK"])
    ],
    dependencies: [],
    targets: [
        .binaryTarget(
            name: "UnifiedConsentSDK",
            url: "https://libraries.osano.com/ios/UnifiedConsentSDK/UnifiedConsentSDK-1.0.0.zip",
            checksum: "a824bc7739e226e1b40ea0f8c4e4f4c6f796fc3b4abfa6e9abe3bd119a30d938"
        ),
    ]
) 