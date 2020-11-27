{ ... }:

{
  nixpkgs = builtins.fetchGit {
    url = "https://github.com/NixOS/nixpkgs.git";
    rev = "43ca7fb8ec1b92cd5cb20d7532f9d6b289d7e7e0";
  };
}
