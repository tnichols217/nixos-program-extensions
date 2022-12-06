{
  description = "Dev shell";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: let
      pkgs = nixpkgs.legacyPackages.${system};
    in {
      devShell = pkgs.mkShell {
        nativeBuildInputs = with pkgs; [
          python310
          python310Packages.requests
        ];
        buildInputs = [ ];
      };
      packages = rec {
        extensions = pkgs.callPackage ./extensions.pkg.nix {};
        default = extensions;
      };
    });
}