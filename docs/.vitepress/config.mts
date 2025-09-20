import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'PFPX Navdata Documentation',
  description: 'Complete guide to PFPX navigation data file format',
  
  // Default language (fallback)
  lang: 'zh-CN',
  
  // Internationalization configuration
  locales: {
    root: {
      label: 'English',
      lang: 'en-US',
      title: 'PFPX Navdata Doc',
      description: 'Complete guide to PFPX navigation data file format',
      themeConfig: {
        nav: [
          { text: 'Home', link: '/' },
          { text: 'Documentation', link: '/guide/' },
          { text: 'Tools', link: '/tools/' }
        ],

        sidebar: {
          '/guide/': [
            {
              text: 'Introduction',
              items: [
                { text: 'Overview', link: '/guide/' },
                { text: 'Getting Started', link: '/guide/getting-started' }
              ]
            },
            {
              text: 'Data Format',
              items: [
                { text: 'File Structure', link: '/guide/file-structure' },
                { text: 'Encoding Table', link: '/guide/encoding-table' },
                { text: 'Decoding Process', link: '/guide/decoding-process' }
              ]
            },
            {
              text: 'Data Sections',
              items: [
                { text: 'File Header', link: '/guide/file-header' },
                { text: 'Runways', link: '/guide/runways' },
                { text: 'Waypoints', link: '/guide/waypoints' },
                { text: 'Airways', link: '/guide/airways' },
                { text: 'SID Procedures', link: '/guide/sid-procedures' },
                { text: 'STAR Procedures', link: '/guide/star-procedures' }
              ]
            },
            {
              text: 'Additional Explanations',
              items: [
                { text: 'Cruise Tables', link: '/guide/cruise-table' }
              ]
            }
          ],
          '/tools/': [
            {
              text: 'Tools',
              items: [
                { text: 'Overview', link: '/tools/' },
                { text: 'Python Decoder', link: '/tools/python-decoder' },
                { text: 'Usage Examples', link: '/tools/examples' }
              ]
            }
          ]
        },

        editLink: {
          pattern: 'https://github.com/6639835/pfpx/edit/main/docs/:path',
          text: 'Edit this page on GitHub'
        },

        footer: {
          message: 'Released under the MIT License.',
          copyright: 'Copyright © 2025 Justin'
        }
      }
    },
    
    zh: {
      label: '简体中文',
      lang: 'zh-CN',
      title: 'PFPX 导航数据文档',
      description: 'PFPX 导航数据文件格式完整指南',
      themeConfig: {
        nav: [
          { text: '首页', link: '/zh/' },
          { text: '文档', link: '/zh/guide/' },
          { text: '工具', link: '/zh/tools/' }
        ],

        sidebar: {
          '/zh/guide/': [
            {
              text: '介绍',
              items: [
                { text: '概述', link: '/zh/guide/' },
                { text: '快速开始', link: '/zh/guide/getting-started' }
              ]
            },
            {
              text: '数据格式',
              items: [
                { text: '文件结构', link: '/zh/guide/file-structure' },
                { text: '编码表', link: '/zh/guide/encoding-table' },
                { text: '解码过程', link: '/zh/guide/decoding-process' }
              ]
            },
            {
              text: '数据段',
              items: [
                { text: '文件头', link: '/zh/guide/file-header' },
                { text: '跑道', link: '/zh/guide/runways' },
                { text: '航路点', link: '/zh/guide/waypoints' },
                { text: '航路', link: '/zh/guide/airways' },
                { text: 'SID 程序', link: '/zh/guide/sid-procedures' },
                { text: 'STAR 程序', link: '/zh/guide/star-procedures' }
              ]
            },
            {
              text: '附加说明',
              items: [
                { text: '巡航表', link: '/zh/guide/cruise-table' }
              ]
            }
          ],
          '/zh/tools/': [
            {
              text: '工具',
              items: [
                { text: '概述', link: '/zh/tools/' },
                { text: 'Python 解码器', link: '/zh/tools/python-decoder' },
                { text: '使用示例', link: '/zh/tools/examples' }
              ]
            }
          ]
        },

        editLink: {
          pattern: 'https://github.com/6639835/pfpx/edit/main/docs/:path',
          text: '在 GitHub 上编辑此页面'
        },

        footer: {
          message: '基于 MIT 许可证发布',
          copyright: '版权所有 © 2025 Justin'
        },

        // Chinese-specific UI text
        outline: {
          label: '页面导航'
        },


        langMenuLabel: '多语言',
        returnToTopLabel: '回到顶部',
        sidebarMenuLabel: '菜单',
        darkModeSwitchLabel: '主题',
        lightModeSwitchTitle: '切换到浅色模式',
        darkModeSwitchTitle: '切换到深色模式'
      }
    }
  },

  // Global theme config (applies to all locales if not overridden)
  themeConfig: {
    logo: './favicon.svg', // Optional: add a logo
    
    socialLinks: [
      { icon: 'github', link: 'https://github.com/6639835/pfpx' }
    ],

    search: {
      provider: 'local',
      options: {
        locales: {
          zh: {
            translations: {
              button: {
                buttonText: '搜索文档',
                buttonAriaLabel: '搜索文档'
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换'
                }
              }
            }
          }
        }
      }
    }
  }
})