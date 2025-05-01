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
            checksum: "b6037fe853db8814291ab370eddf2f13ba9a6bd4f9aacfa40e4466f5f7fb05c3"
        ),
    ]
) 