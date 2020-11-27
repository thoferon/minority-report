let
  nixpkgs = import ./nixpkgs {};

  inherit (nixpkgs) pkgs;

  pythonPackages = import ./python { inherit pkgs; };

in
pkgs.mkShell {
  buildInputs = with pkgs; [
  ] ++ pythonPackages;
}
