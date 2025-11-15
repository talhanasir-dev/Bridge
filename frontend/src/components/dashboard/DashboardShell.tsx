import { ReactNode, CSSProperties } from "react";
import {
  Baby,
  Bell,
  CircleHelp,
  LucideIcon,
  LogOut,
  MessageSquarePlus,
  Plus,
  Settings,
} from "lucide-react";

import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarGroup,
  SidebarGroupLabel,
  SidebarHeader,
  SidebarInset,
  SidebarMenu,
  SidebarMenuBadge,
  SidebarMenuButton,
  SidebarMenuItem,
  SidebarProvider,
  SidebarSeparator,
  SidebarTrigger,
  useSidebar,
} from "@/components/ui/sidebar";
import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Avatar, AvatarFallback } from "@/components/ui/avatar";
import { cn } from "@/lib/utils";

type DashboardNavItem = {
  id: string;
  label: string;
  icon: LucideIcon;
  badge?: string | number;
  tone?: "default" | "alert";
};

type DashboardShellProps = {
  children: ReactNode;
  navItems: DashboardNavItem[];
  activeItem: string;
  onNavigate: (id: string) => void;
  onLogout: () => void;
  onOpenSettings: () => void;
  onOpenChildren?: () => void;
  onCreateQuickAction?: () => void;
  onOpenMessages?: () => void;
  currentUser?: { firstName: string; lastName: string; email: string } | null;
  heroSubtitle?: string;
};

const DashboardNavigation = ({
  navItems,
  activeItem,
  onNavigate,
}: {
  navItems: DashboardNavItem[];
  activeItem: string;
  onNavigate: (id: string) => void;
}) => {
  const { setOpenMobile } = useSidebar();

  return (
    <SidebarGroup className="px-3">
      <SidebarGroupLabel className="text-xs uppercase tracking-[0.2em] text-white/70">
        Navigate
      </SidebarGroupLabel>
      <SidebarMenu>
        {navItems.map((item) => (
          <SidebarMenuItem key={item.id}>
            <SidebarMenuButton
              className={cn(
                "text-white/90 hover:text-white",
                item.tone === "alert" && "text-orange-100 data-[active=true]:text-white"
              )}
              isActive={activeItem === item.id}
              onClick={() => {
                onNavigate(item.id);
                setOpenMobile(false);
              }}
            >
              <item.icon className="h-4 w-4" />
              <span>{item.label}</span>
            </SidebarMenuButton>
            {item.badge && (
              <SidebarMenuBadge className="bg-white/10 text-white">
                {item.badge}
              </SidebarMenuBadge>
            )}
          </SidebarMenuItem>
        ))}
      </SidebarMenu>
    </SidebarGroup>
  );
};

const DashboardShell = ({
  children,
  navItems,
  activeItem,
  onNavigate,
  onLogout,
  onOpenSettings,
  onOpenChildren,
  onCreateQuickAction,
  onOpenMessages,
  currentUser,
  heroSubtitle = "Fair & balanced co-parenting",
}: DashboardShellProps) => {
  const activeLabel =
    navItems.find((item) => item.id === activeItem)?.label ?? "Overview";

  const initials = currentUser
    ? `${currentUser.firstName?.[0] ?? ""}${currentUser.lastName?.[0] ?? ""}` ||
      currentUser.email?.[0] ||
      "B"
    : "B";

  const sidebarTheme: CSSProperties = {
    "--sidebar-background": "225 27% 12%",
    "--sidebar-foreground": "210 40% 96%",
    "--sidebar-accent": "222 47% 20%",
    "--sidebar-accent-foreground": "210 40% 98%",
    "--sidebar-border": "222 36% 16%",
    "--sidebar-ring": "215 83% 53%",
  };

  return (
    <SidebarProvider defaultOpen>
      <div className="bg-slate-950 text-white">
        <Sidebar
          className="bg-gradient-to-b from-slate-950 via-slate-900 to-slate-900 text-white border-none"
          style={sidebarTheme}
        >
          <SidebarHeader className="px-4 pt-5 pb-3">
            <div className="flex items-center gap-3">
              <img
                src="/bridge-avatar.png"
                alt="Bridge"
                className="h-8 w-8 rounded-full bg-white/10 p-1"
              />
              <div>
                <p className="text-base font-semibold tracking-tight">Bridge</p>
                <p className="text-xs text-white/70">{heroSubtitle}</p>
              </div>
            </div>
          </SidebarHeader>
          <SidebarContent className="gap-6">
            <DashboardNavigation
              navItems={navItems}
              activeItem={activeItem}
              onNavigate={onNavigate}
            />
            <SidebarSeparator className="bg-white/10" />
            <SidebarGroup className="px-3">
              <SidebarGroupLabel className="text-xs uppercase tracking-[0.2em] text-white/70">
                Quick actions
              </SidebarGroupLabel>
              <SidebarMenu>
                <SidebarMenuItem>
                  <SidebarMenuButton
                    onClick={() => onCreateQuickAction?.()}
                    className="text-white/90 hover:text-white"
                  >
                    <Plus className="h-4 w-4" />
                    New request
                  </SidebarMenuButton>
                </SidebarMenuItem>
                <SidebarMenuItem>
                  <SidebarMenuButton
                    onClick={() => onOpenMessages?.()}
                    className="text-white/90 hover:text-white"
                  >
                    <MessageSquarePlus className="h-4 w-4" />
                    Message partner
                  </SidebarMenuButton>
                </SidebarMenuItem>
                <SidebarMenuItem>
                  <SidebarMenuButton className="text-white/90 hover:text-white">
                    <CircleHelp className="h-4 w-4" />
                    Need help?
                  </SidebarMenuButton>
                </SidebarMenuItem>
              </SidebarMenu>
            </SidebarGroup>
          </SidebarContent>
          <SidebarFooter className="p-3 border-t border-white/10">
            <Button
              variant="ghost"
              size="sm"
              className="w-full justify-start text-white/80 hover:text-white hover:bg-white/10"
              onClick={onOpenSettings}
            >
              <Settings className="mr-2 h-4 w-4" />
              Settings
            </Button>
            <Button
              variant="ghost"
              size="sm"
              className="w-full justify-start text-white/80 hover:text-white hover:bg-white/10"
              onClick={onLogout}
            >
              <LogOut className="mr-2 h-4 w-4" />
              Logout
            </Button>
          </SidebarFooter>
        </Sidebar>
      </div>
      <SidebarInset className="bg-slate-50">
        <header className="flex h-16 items-center border-b border-slate-200 bg-white px-4 md:px-8">
          <div className="flex items-center gap-3">
            <SidebarTrigger className="text-slate-600 hover:text-slate-900" />
            <div>
              <p className="text-xs uppercase tracking-[0.3em] text-slate-400">
                Bridge workspace
              </p>
              <h1 className="text-lg font-semibold text-slate-900">
                {activeLabel}
              </h1>
            </div>
          </div>
          <div className="ml-6 hidden flex-1 items-center gap-2 rounded-xl bg-slate-100 px-3 py-1 md:flex">
            <Input
              placeholder="Search calendar, expenses, or documents"
              className="h-8 border-none bg-transparent text-sm shadow-none focus-visible:ring-0"
            />
          </div>
          <div className="ml-auto flex items-center gap-2">
            <Button
              variant="outline"
              size="sm"
              className="hidden md:inline-flex border-slate-200 text-slate-700"
              onClick={() => onCreateQuickAction?.()}
            >
              <Plus className="mr-2 h-4 w-4" />
              Quick add
            </Button>
            {onOpenChildren && (
              <Button
                variant="outline"
                size="sm"
                className="border-green-200 text-green-700"
                onClick={onOpenChildren}
              >
                <Baby className="mr-2 h-4 w-4" />
                Manage kids
              </Button>
            )}
            <Button
              variant="ghost"
              size="icon"
              className="text-slate-600"
              onClick={() => onOpenMessages?.()}
            >
              <Bell className="h-4 w-4" />
              <span className="sr-only">Notifications</span>
            </Button>
            <Avatar className="h-9 w-9 border border-slate-100">
              <AvatarFallback className="bg-slate-900 text-white text-sm">
                {initials.toUpperCase()}
              </AvatarFallback>
            </Avatar>
          </div>
        </header>
        <div className="flex-1 overflow-y-auto bg-gradient-to-br from-slate-50 via-white to-blue-50 px-4 py-6 md:px-8">
          <div className="mx-auto w-full max-w-6xl space-y-6">{children}</div>
        </div>
      </SidebarInset>
    </SidebarProvider>
  );
};

export type { DashboardNavItem };
export default DashboardShell;

