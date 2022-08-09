{ pkgs }:

pkgs.stdenv.mkDerivation rec {
  pname = "nixos-program-extensions";
  version = "v1.0.0";

  src = ./.;

  nativeBuildInputs = with pkgs; [
    python310
    python310Packages.requests
  ];

  buildPhase =
  ''

  cd firefox
  python updateFirefoxExtensions.py
  cd ../vscode
  python updateVSCodeExtensions.py

  '';

  installPhase = 
  ''

  mkdir $out

  cp -r firefox/out $out/firefox
  cp -r vscode/out $out/vscode

  '';

  meta = {
    description = "Nixos program extensions";
    homepage = "https://github.com/tnichols217/nixos-program-extensions";
    license = pkgs.lib.licenses.gpl3;
    platforms = pkgs.lib.platforms.all;
  };
}